from infrastructure.db_repository import insert_later_movie, get_watchlater_ids_by_user
from infrastructure.tmdb_api import get_movie_by_id

def add_later_movie_use_case(user_id, movie_id):
    return insert_later_movie(user_id, movie_id)

def get_later_movie_use_case(user_id):
    movie_ids = get_watchlater_ids_by_user(user_id)
    watchlater_responses = []

    for movie_id in movie_ids:
        movie_data = get_movie_by_id(movie_id)

        if movie_data and movie_data.get("id") and movie_data.get("poster"):
            watchlater_responses.append({
                "id": movie_data["id"],
                "poster": movie_data["poster"]
            })

    return watchlater_responses