import requests
from django.conf import settings

BASE_URL = "https://api.rawg.io/api/games"

def fetch_games(params=None):
    params = params or {}
    params["key"] = settings.RAWG_API_KEY

    response = requests.get(BASE_URL, params=params, timeout=10)
    response.raise_for_status()
    return response.json()
