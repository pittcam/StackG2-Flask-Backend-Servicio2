from infrastructure.db_repository import insert_favorite_movie, get_favorite_movie_ids_by_user
from infrastructure.tmdb_api import get_movie_by_id

def add_favorite_movie_use_case(user_id, movie_id):
    return insert_favorite_movie(user_id, movie_id)

def get_favorite_movie_use_case(user_id):
    movie_ids = get_favorite_movie_ids_by_user(user_id)
    favorite_responses = []

    for movie_id in movie_ids:
        movie_data = get_movie_by_id(movie_id)

        if movie_data and movie_data.get("id") and movie_data.get("poster"):
            favorite_responses.append({
                "id": movie_data["id"],
                "poster": movie_data["poster"]
            })

    return favorite_responses