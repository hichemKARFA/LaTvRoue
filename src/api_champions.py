# src/api_champions.py

import requests

class RiotAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://ddragon.leagueoflegends.com/cdn"

    def get_champions(self, version="12.1.1", language="fr_FR"):
        """Récupère la liste des champions via l'API."""
        url = f"{self.base_url}/{version}/data/{language}/champion.json"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Erreur lors de la récupération des champions: {response.status_code}")

