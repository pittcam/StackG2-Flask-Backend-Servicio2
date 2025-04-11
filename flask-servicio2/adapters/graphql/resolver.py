from ariadne import QueryType
from application.use_cases.search_movies import search_movies_use_case

query = QueryType()

@query.field("searchMovies")
def resolve_search_movies(_, info, query):
    return search_movies_use_case(query)