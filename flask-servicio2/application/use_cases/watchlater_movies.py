from infrastructure.db_repository import insert_later_movie

def add_later_movie_use_case(user_id, movie_id):
    return insert_later_movie(user_id, movie_id)
