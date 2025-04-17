import psycopg2
import os

def get_connection():
    return psycopg2.connect(
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host=os.getenv("POSTGRES_HOST"),
        port=os.getenv("POSTGRES_PORT"),
    )

def insert_favorite_movie(user_id, movie_id):
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute(
            "INSERT INTO user_favorites (user_id, movie_id) VALUES (%s, %s) ON CONFLICT DO NOTHING",
            (user_id, movie_id),
        )
        conn.commit()
        return {"success": True, "movie_id": movie_id}
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cur.close()
        conn.close()

def insert_later_movie(user_id, movie_id):
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute(
            "INSERT INTO user_favorites (user_id, movie_id) VALUES (%s, %s) ON CONFLICT DO NOTHING",
            (user_id, movie_id),
        )
        conn.commit()
        return {"success": True, "movie_id": movie_id}
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cur.close()
        conn.close()

  # depende de cómo conectes

def get_favorite_movie_ids_by_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT movie_id FROM user_favorites WHERE user_id = %s", (user_id,))
        rows = cursor.fetchall()
        return [row[0] for row in rows]
    finally:
        cursor.close()
        conn.close()
