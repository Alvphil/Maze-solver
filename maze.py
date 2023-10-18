from cell import Cell
from graphics import Point
from time import sleep
import random

class Maze:
    def __init__(self, x1, y1, num_rows, nom_columns, cell_size_x, cell_size_y, win=None, seed=None) :
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_columns = nom_columns
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        self.visited = False
        #if seed is None:
        self.seed = random.seed(seed)
        #else:
            #self.seed = seed
        self._create_cells()

    def _create_cells(self):
        offsett = self.x1
        for i in range(self.num_rows):
            self._cells.append([])#= []
            for j in range(self.num_columns):
                self._cells[i].append(self._break_entrance_and_exit(i,j)) #Cell(self.win))      # [j] #= Cell(self.win)
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        p1 = Point(self.x1 + j * self.cell_size_x , self.y1 + i * self.cell_size_y)
        p2 = Point(p1.x + self.cell_size_x, p1.y + self.cell_size_y)
        self._cells[i][j].draw(p1, p2)
        self._animate()

    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        sleep(0.05)

    def _break_entrance_and_exit(self,i,j):
        if i == 0 and j == 0:
            return Cell(self.win, False)
        elif i == self.num_rows-1 and j == self.num_columns-1:
            return Cell(self.win,True ,False)
        else:
            return Cell(self.win)
    
    def _reset_cells_visited(self):
        for i in range(self.num_rows):
            for j in range(self.num_columns):
                self._cells[i][j].visited = False

    def _break_walls_r(self, i, j):
        self.cell[i][j].visited = True
        while True:

            next_index_list = []

            possible_direction_indexes = 0

            # determine which cell(s) to visit next
            # left
            if i > 0 and not self._cells[i - 1][j].visited:
                next_index_list.append((i - 1, j))
                possible_direction_indexes += 1
            # right
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                next_index_list.append((i + 1, j))
                possible_direction_indexes += 1
            # up
            if j > 0 and not self._cells[i][j - 1].visited:
                next_index_list.append((i, j - 1))
                possible_direction_indexes += 1
            # down
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                next_index_list.append((i, j + 1))
                possible_direction_indexes += 1

            # if there is nowhere to go from here
            # just break out
            if possible_direction_indexes == 0:
                self._draw_cell(i, j)
                return

            # randomly choose the next direction to go
            direction_index = random.randrange(possible_direction_indexes)
            next_index = next_index_list[direction_index]

            # knock out walls between this cell and the next cell(s)
            # right
            if next_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            # left
            if next_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            # down
            if next_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            # up
            if next_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False

            # recursively visit the next cell
            self._break_walls_r(next_index[0], next_index[1])
            self._reset_cells_visited()

