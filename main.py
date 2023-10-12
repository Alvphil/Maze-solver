from cell import Cell
from graphics import Window, Point
from maze import Maze
import time



def main():
    win = Window(800, 600)
    #cell_1 = Cell(win)
    #cell_1.draw(Point(20, 500), Point(300, 20))
    #cell_2 = Cell(win)
    #cell_2.draw(Point(60,600), Point(100,450))
    #cell_1.draw_move(cell_2)
    maze_1 = Maze(1,1,8,6,100,100,win)
    win.wait_for_close()

    


main()