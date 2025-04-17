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

def get_movie_by_id(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    params = {
        "api_key": TMDB_API_KEY,
        "language": "es-ES"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        return {
            "id": data["id"],
            "poster": f"https://image.tmdb.org/t/p/w500{data.get('poster_path')}" if data.get("poster_path") else None
        }

    return None