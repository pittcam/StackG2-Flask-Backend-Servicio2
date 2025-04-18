from ariadne import QueryType, MutationType
from application.use_cases.search_movies import search_movies_use_case
from application.use_cases.watchlater_movies import add_later_movie_use_case, get_later_movie_use_case
from application.use_cases.favorites_movies import add_favorite_movie_use_case, get_favorite_movie_use_case

query = QueryType()
mutation = MutationType()

@query.field("searchMovies")
def resolve_search_movies(_, info, query):
    return search_movies_use_case(query)

@mutation.field("addFavoriteMovie")
def resolve_add_favorite_movie(_, info, user_id, movie_id):
    try:
        result = add_favorite_movie_use_case(user_id, movie_id)
        return {"success": result["success"], "movie_id": result["movie_id"]}
    except Exception as e:
        print("Error:", e)
        return {"success": False, "movie_id": movie_id}


@mutation.field("addToWatchLater")
def resolve_add_watchlater_movie(_, info, user_id, movie_id):
    try:
        result = add_later_movie_use_case(user_id, movie_id)
        return {"success": result["success"], "movie_id": result["movie_id"]}
    except Exception as e:
        print("Error:", e)
        return {"success": False, "movie_id": movie_id}

@query.field("getFavoriteMovies")
def resolve_get_favorite_movies(_, info, user_id):
    try:
        return get_favorite_movie_use_case(user_id)
    except Exception as e:
        print("Error:", e)
        return []

@query.field("getWatchLaterMovies")
def resolve_get_later_movies(_, info, user_id):
    try:
        return get_later_movie_use_case(user_id)
    except Exception as e:
        print("Error:", e)
        return []