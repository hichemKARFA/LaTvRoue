# Factory Pattern pour la création de matchs
class MatchFactory:
    @staticmethod
    def creer_match(equipe1, equipe2, champion_pool, roles_disponibles):
        # Assigner les rôles et les champions aux joueurs
        equipe1.assigner_roles(roles_disponibles)
        equipe2.assigner_roles(roles_disponibles)
        equipe1.assigner_champions(champion_pool)
        equipe2.assigner_champions(champion_pool)

        # Créer et retourner un match
        return Match(equipe1, equipe2)


# Classe Match pour représenter une partie entre deux équipes
class Match:
    def __init__(self, equipe1, equipe2):
        self.equipe1 = equipe1
        self.equipe2 = equipe2

    def afficher_match(self):
        """Affiche les équipes et les joueurs assignés à chaque rôle et champion."""
        print("Équipe 1:")
        self.equipe1.afficher_equipe()
        print("\nÉquipe 2:")
        self.equipe2.afficher_equipe()

    def enregistrer_resultat(self, gagnant):
        """Enregistre le gagnant du match (1 ou 2)."""
        print(f"L'équipe {gagnant} a gagné le match !")
