# Classe Historique pour enregistrer les résultats des matchs
class Historique:
    def __init__(self):
        self.matchs = []

    def ajouter_match(self, match, gagnant):
        """Ajoute un match à l'historique avec le gagnant."""
        self.matchs.append({'match': match, 'gagnant': gagnant})

    def afficher_historique(self):
        """Affiche l'historique des matchs joués."""
        for i, data in enumerate(self.matchs):
            print(f"Match {i + 1}:")
            data['match'].afficher_match()
            print(f"Gagnant: Équipe {data['gagnant']}")
