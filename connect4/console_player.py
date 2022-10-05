from .game import Grid, Player


class ConsolePlayer(Player):
    """Allow a human to see the grid in its shell, and input a column from the
    keyboard."""

    def play(self, grid: Grid) -> int:
        num_col = int(input("Num colonne: ")) #saisir une colonne sur le clavier
        return num_col # retourne le numéro de la colonne 
     
        
