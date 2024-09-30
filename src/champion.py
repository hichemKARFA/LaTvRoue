import random
import requests

class Champion:
    def __init__(self, nom, role):
        self.nom = nom
        self.role = role

    def afficher_details(self):
        print(f"Champion: {self.nom}, Rôle: {self.role}")


class ChampionPool:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ChampionPool, cls).__new__(cls)
            cls._instance.champions = []
            cls._instance.charger_champions_depuis_api()  # Charger la liste des champions via l'API
        return cls._instance

    def ajouter_champion(self, champion):
        """Ajoute un champion à la pool disponible."""
        self.champions.append(champion)

    def tirer_champion_disponible(self):
        """Tire un champion aléatoire de la pool et le retire pour éviter les doublons."""
        if self.champions:
            return self.champions.pop(random.randint(0, len(self.champions) - 1))
        else:
            raise ValueError("Aucun champion disponible.")

    def afficher_champions_disponibles(self):
        """Affiche la liste des champions encore disponibles."""
        for champion in self.champions:
            print(f"{champion.nom} ")

    def charger_champions_depuis_api(self):
        """Charge la liste des champions depuis l'API Riot Games (Data Dragon)"""
        try:
            # Récupérer la dernière version du jeu
            version_url = "https://ddragon.leagueoflegends.com/api/versions.json"
            version_response = requests.get(version_url)
            if version_response.status_code == 200:
                latest_version = version_response.json()[0]
                print(f"Version actuelle : {latest_version}")
            else:
                print("Impossible de récupérer la version actuelle.")
                return

            # Récupérer la liste des champions pour la dernière version
            lang = "fr_FR"  # Changer si tu veux une autre langue
            champions_url = f"https://ddragon.leagueoflegends.com/cdn/{latest_version}/data/{lang}/champion.json"
            champions_response = requests.get(champions_url)

            if champions_response.status_code == 200:
                champions_data = champions_response.json()["data"]

                # Extraire chaque champion de la réponse et l'ajouter à la pool
                for champion_key, champion_info in champions_data.items():
                    nom = champion_info["name"]
                    roles = champion_info["tags"]
                    role = roles[0] if roles else "Unknown"  # Utiliser le premier rôle s'il y en a plusieurs
                    champion = Champion(nom, role)
                    self.ajouter_champion(champion)
                print(f"Nombre de champions chargés : {len(self.champions)}")
            else:
                print("Erreur lors de la récupération des champions.")
        except Exception as e:
            print(f"Une erreur s'est produite lors du chargement des champions : {e}")
