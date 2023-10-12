from cell import Cell
from graphics import Window, Point
from maze import Maze
import time



def main():
    num_rows = 12
    num_cols = 16
    margin = 20
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)
    #cell_1 = Cell(win)
    #cell_1.draw(Point(20, 500), Point(300, 20))
    #cell_2 = Cell(win)
    #cell_2.draw(Point(60,600), Point(100,450))
    #cell_1.draw_move(cell_2)
    maze_1 = Maze(margin,margin,num_rows,num_cols,cell_size_x,cell_size_y,win)
    win.wait_for_close()

    


main()