from cell import Cell
from graphics import Point

class Maze:
    def __init__(self, x1, y1, num_rows, nom_columns, cell_size_x, cell_size_y, win):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_columns = nom_columns
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        for i in range(self.num_columns):
            self._cells.append([])#= []
            self.x1 = 1
            for j in range(self.num_rows):
                self._cells[i].append(Cell(self.win))      # [j] #= Cell(self.win)
                self._draw_cell(i, j)
                self.x1 =  (j+1) * self.cell_size_x
                print(self.x1)
            self.y1 = (i+1) * self.cell_size_y 

    def _draw_cell(self, i, j):
        p1 = Point(self.x1, self.y1)
        p2 = Point(p1.x + self.cell_size_x, p1.y + self.cell_size_y)
        self._cells[i][j].draw(p1, p2)

