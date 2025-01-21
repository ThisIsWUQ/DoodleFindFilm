# reference: https://github.com/TharinduMadhusanka/semantic-movie-search/blob/main/YTS_url.py
# ---------------------------------------------------------------------------------
# Get a Result through API
import requests

def get_movie_page_url(movie_name):
    base_url = "https://yts.mx/api/v2/list_movies.json"

    params = {
        "query_term": movie_name,
        "limit": 1  # Limiting to 1 result as only need the page URL of one movie
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()

        data = response.json()

        # Extracting the page URL of the movie (if available)
        if data["status"] == "ok" and data["data"]["movie_count"] > 0:
            movie_url = data["data"]["movies"][0]["url"]
            return movie_url
        else:
            return None

    except requests.RequestException as e:
        print("Error fetching data:", e)
        return None