from flask import Flask, request, jsonify
from ariadne import graphql_sync, make_executable_schema
from ariadne.explorer import ExplorerGraphiQL
from adapters.graphql.schema import type_defs
from adapters.graphql.resolver import query, mutation
from flask_cors import CORS
import os
from dotenv import load_dotenv
from database.init_db import init_db


init_db()
load_dotenv()


app = Flask(__name__)
CORS(app)

schema = make_executable_schema(type_defs, query, mutation)

@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return ExplorerGraphiQL().html(None), 200

@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(schema, data, context_value=request, debug=True)
    return jsonify(result), 200 if success else 400

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True, port=5001)
