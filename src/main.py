from champion import ChampionPool
from joueur import Joueur
from equipe import Equipe
from match import MatchFactory

def main():
    # Définir les rôles possibles
    roles_disponibles = ['Top', 'Jungle', 'Mid', 'ADC', 'Support']

    # Créer la pool de champions et charger les champions depuis l'API
    champion_pool = ChampionPool()

    # Créer les équipes
    equipe1 = Equipe()
    equipe2 = Equipe()

    # Ajouter des joueurs aux équipes
    equipe1.ajouter_joueur(Joueur("Joueur1"))
    equipe1.ajouter_joueur(Joueur("Joueur2"))
    equipe1.ajouter_joueur(Joueur("Joueur3"))
    equipe1.ajouter_joueur(Joueur("Joueur4"))
    equipe1.ajouter_joueur(Joueur("Joueur5"))

    equipe2.ajouter_joueur(Joueur("Joueur6"))
    equipe2.ajouter_joueur(Joueur("Joueur7"))
    equipe2.ajouter_joueur(Joueur("Joueur8"))
    equipe2.ajouter_joueur(Joueur("Joueur9"))
    equipe2.ajouter_joueur(Joueur("Joueur10"))

    # Créer le match via la Factory
    match = MatchFactory.creer_match(equipe1, equipe2, champion_pool, roles_disponibles)

    # Afficher les équipes et les champions assignés
    match.afficher_match()

    champion_pool.afficher_champions_disponibles()

if __name__ == "__main__":
    main()
