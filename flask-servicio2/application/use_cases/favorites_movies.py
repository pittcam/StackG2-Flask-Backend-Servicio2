from infrastructure.db_repository import insert_favorite_movie

def add_favorite_movie_use_case(user_id, movie_id):
    return insert_favorite_movie(user_id, movie_id)
