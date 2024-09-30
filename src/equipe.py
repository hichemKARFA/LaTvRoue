import random

# Classe Equipe qui gère une liste de joueurs et leur assignation de rôles et de champions
class Equipe:
    def __init__(self):
        self.joueurs = []

    def ajouter_joueur(self, joueur):
        """Ajoute un joueur à l'équipe."""
        self.joueurs.append(joueur)

    def assigner_roles(self, roles_disponibles):
        """Assigne des rôles aléatoires aux joueurs."""
        random.shuffle(roles_disponibles)
        for joueur, role in zip(self.joueurs, roles_disponibles):
            joueur.assigner_role(role)

    def assigner_champions(self, champion_pool):
        """Assigne des champions aux joueurs sans doublons."""
        for joueur in self.joueurs:
            champion = champion_pool.tirer_champion_disponible()
            joueur.assigner_champion(champion)

    def afficher_equipe(self):
        """Affiche les détails de l'équipe."""
        for joueur in self.joueurs:
            joueur.afficher_details()
