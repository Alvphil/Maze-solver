from cell import Cell
from graphics import Window, Point
import time



def main():
    win = Window(800, 600)
    cell_1 = Cell(win)
    cell_1.draw(Point(20, 500), Point(300, 20))
    cell_2 = Cell(win)
    cell_2.draw(Point(60,600), Point(100,450))
    cell_1.draw_move(cell_2)
    win.wait_for_close()

    


main()