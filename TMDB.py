# Connect API
# reference: https://github.com/TharinduMadhusanka/semantic-movie-search/blob/main/TMDB.py
# ---------------------------------------------------------------------------------
import requests
import streamlit as st

api_key = st.secrets['api_key']

def api_response(movie_id):
    search_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"
    response = requests.get(search_url)
    data = response.json()

    if response.status_code != 200:
        print("Error fetching data:", response.text)
        return None

    image_url = f"https://image.tmdb.org/t/p/w500{data['poster_path']}"
    backdrop_url = f"https://image.tmdb.org/t/p/w500{data['backdrop_path']}"

    data["poster_url"] = image_url 
    data["backdrop_url"] = backdrop_url
    data["imdb_url"] = f"https://www.imdb.com/title/{data['imdb_id']}" if data["imdb_id"] else None

    return data
# ---------------------------------------------------------------------------------
