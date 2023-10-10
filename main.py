from tkinter import Tk, BOTH,Canvas
import time

class Window:
    def __init__(self, width, height):
  
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__window = Canvas(self.__root, bg="white",width=width,height=height)
        self.__window.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running == True:
            self.redraw()
        print("window closed")

    def close(self):
        self.__running = False

    def draw_line(self,line, color):
        line.draw(self.__window, color)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1  #Start position in x, y
        self.p2 = p2    #last position in x, y
    
    def draw(self, canvas, color):
        x1, y1 = self.p1.x, self.p1.y
        x2, y2 = self.p2.x, self.p2.y
        canvas.create_line(x1, y1, x2, y2, fill=color, width=2)

class Cell:
    def __init__(self, win,
                 has_left_wall=True,
                 has_right_wall=True,
                 has_top_wall=True,
                 has_bottom_wall=True,
                 #top_left, bottom_right,
                 ):
        
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self.__top_left = 0   #top_left.x
        self.__top_right = 0   #bottom_right.x
        self.__bottom_left = 0   #top_left.y
        self.__bottom_right = 0   #bottom_right.y
        self.__win = win

    def draw(self, top_left_point, bottom_right_point):
            self.__top_left = top_left_point
            self.__bottom_right = bottom_right_point
            self.__top_right = Point(bottom_right_point.x, top_left_point.y)
            self.__bottom_left = Point(top_left_point.x, bottom_right_point.y)
            if self.has_top_wall:
                self.__win.draw_line(Line(self.__top_left, self.__top_right), "black")
            if self.has_right_wall:
                self.__win.draw_line(Line(self.__top_right, self.__bottom_right), "black")
            if self.has_bottom_wall:
                self.__win.draw_line(Line(self.__bottom_left, self.__bottom_right), "black")
            if self.has_left_wall:
                self.__win.draw_line(Line(self.__top_left, self.__bottom_left), "black")
def main():
    win = Window(800, 600)
    line = Line(Point(20,20),Point(500,500))
    cell_1 = Cell(win)
    cell_1.draw(Point(20, 500), Point(300, 20))
    win.draw_line(line, "red")
    win.wait_for_close()

    


main()