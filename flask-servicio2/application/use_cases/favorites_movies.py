from infrastructure.db_repository import insert_favorite_movie
from infrastructure.db_repository import get_favorite_movie

def add_favorite_movie_use_case(user_id, movie_id):
    return insert_favorite_movie(user_id, movie_id)

def get_favorite_movie_use_case(user_id, movie_id):
    return get_favorite_movie(user_id)