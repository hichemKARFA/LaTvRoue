import json
import random
from joueur import Joueur

def charger_joueurs_depuis_json_aleatoire(fichier_json, nombre_joueurs=10):
    """
    Charge une liste de joueurs depuis un fichier JSON et sélectionne aléatoirement un sous-ensemble.
    :param fichier_json: Chemin vers le fichier JSON contenant la liste des joueurs
    :param nombre_joueurs: Le nombre de joueurs à sélectionner aléatoirement
    :return: Une liste de joueurs sélectionnés aléatoirement
    """
    try:
        with open(fichier_json, 'r') as f:
            data = json.load(f)
            tous_les_joueurs = [Joueur(joueur_data["pseudo"]) for joueur_data in data["joueurs"]]

            # Si moins de joueurs que nécessaire, lever une exception
            if len(tous_les_joueurs) < nombre_joueurs:
                raise ValueError(f"Pas assez de joueurs dans le fichier. Il en faut au moins {nombre_joueurs}.")

            # Sélectionner aléatoirement 10 joueurs parmi tous
            joueurs_selectionnes = random.sample(tous_les_joueurs, nombre_joueurs)

            return joueurs_selectionnes
    except FileNotFoundError:
        print(f"Erreur : Le fichier {fichier_json} n'existe pas.")
        return []
    except json.JSONDecodeError:
        print(f"Erreur : Le fichier {fichier_json} contient une erreur de format.")
        return []
