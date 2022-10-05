from .game import Grid, Player


class ConsolePlayer(Player):
    """Allow a human to see the grid in its shell, and input a column from the
    keyboard."""

    def play(self, grid: Grid) -> int:
        saisie_col = int(input("Num colonne:")) #saisir une colonne sur le clavier
        return saisie_col # retourner la grille
     
        
