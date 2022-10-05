from .game import Grid, Player,Cell

class DumbIA(Player):
    def play(self, grid: Grid) -> int:
       for line in range(grid.lines): 
          for column in range(grid.columns): 
            if grid.grid[line][column] == Cell.EMPTY : # vérifier si la cellule est vide
                return column # retourne le numéro de la colonne
