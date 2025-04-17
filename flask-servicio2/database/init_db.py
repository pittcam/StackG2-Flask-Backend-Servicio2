import psycopg2
import os

sql_script = """
CREATE TABLE IF NOT EXISTS user_favorites (
    user_id UUID NOT NULL,
    movie_id VARCHAR NOT NULL,
    PRIMARY KEY (user_id, movie_id)
);

CREATE TABLE IF NOT EXISTS user_watchlist (
    user_id UUID NOT NULL,
    movie_id VARCHAR NOT NULL,
    PRIMARY KEY (user_id, movie_id)
);
"""

def init_db():
    conn = psycopg2.connect(
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host=os.getenv("POSTGRES_HOST"),
        port=os.getenv("POSTGRES_PORT"),
    )
    cur = conn.cursor()
    try:
        cur.execute(sql_script)
        conn.commit()
    finally:
        cur.close()
        conn.close()

if __name__ == "__main__":
    init_db()
