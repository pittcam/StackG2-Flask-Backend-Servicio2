import os
import requests
from dotenv import load_dotenv

load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY")


def search_movies(query):
    url = "https://api.themoviedb.org/3/search/movie"
    params = {
        "api_key": TMDB_API_KEY,
        "query": query
    }
    res = requests.get(url, params=params)
    data = res.json()

    # Mapeamos los datos al tipo Movie
    movies = data.get("results", [])
    return [
        {
            "id": movie["id"],
            "title": movie["title"],
            "overview": movie.get("overview"),
            "release_date": movie.get("release_date"),
            "poster": f"https://image.tmdb.org/t/p/w500{movie.get('poster_path')}" if movie.get("poster_path") else None
        }
        for movie in movies
    ]