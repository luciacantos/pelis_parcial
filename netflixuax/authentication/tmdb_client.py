import requests
from django.conf import settings

TMDB_API_BASE_URL = "https://api.themoviedb.org/3"

def get_tmdb_data(endpoint, params={}):
    params['api_key'] = settings.TMDB_API_KEY
    url = f"{TMDB_API_BASE_URL}/{endpoint}"
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()
