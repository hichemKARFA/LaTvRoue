import random  # Assurez-vous que ce module est importé correctement
from champion import ChampionPool
from equipe import Equipe
from match import MatchFactory
from charger_joueurs_depuis_json import charger_joueurs_depuis_json_aleatoire

def main():
    # Charger 10 joueurs aléatoires depuis le fichier JSON
    liste_joueurs = charger_joueurs_depuis_json_aleatoire('joueurs.json', 10)

    # Mélanger les joueurs aléatoirement
    random.shuffle(liste_joueurs)

    # Diviser les joueurs en deux équipes aléatoires
    equipe1 = Equipe()
    equipe2 = Equipe()

    # Ajouter les 5 premiers joueurs à l'équipe 1 et les 5 suivants à l'équipe 2
    for i in range(5):
        equipe1.ajouter_joueur(liste_joueurs[i])
    for i in range(5, 10):
        equipe2.ajouter_joueur(liste_joueurs[i])

    # Définir les rôles possibles
    roles_disponibles = ['Top', 'Jungle', 'Mid', 'ADC', 'Support']

    # Créer la pool de champions
    champion_pool = ChampionPool()

    # Créer le match via la Factory
    match = MatchFactory.creer_match(equipe1, equipe2, champion_pool, roles_disponibles)

    # Afficher les équipes et les champions assignés
    match.afficher_match()

if __name__ == "__main__":
    main()
