# Classe Joueur qui contient un pseudo, un rôle et un champion attribué
class Joueur:
    def __init__(self, pseudo):
        self.pseudo = pseudo
        self.role = None  # Le rôle sera assigné plus tard
        self.champion = None  # Le champion sera assigné plus tard

    def assigner_role(self, role):
        """Assigne un rôle au joueur."""
        self.role = role

    def assigner_champion(self, champion):
        """Assigne un champion au joueur."""
        self.champion = champion

    def afficher_details(self):
        """Affiche les détails du joueur, y compris le rôle et le champion."""
        if self.champion:
            print(f"Joueur: {self.pseudo}, Rôle: {self.role}, Champion: {self.champion.nom}")
        else:
            print(f"Joueur: {self.pseudo}, Rôle: {self.role}, Champion: Non attribué")
