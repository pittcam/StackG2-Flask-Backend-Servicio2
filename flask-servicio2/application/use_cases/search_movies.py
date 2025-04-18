from adapters.out.tmdb_api import search_movies

def search_movies_use_case(query):
    return search_movies(query)