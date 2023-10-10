from tkinter import Tk, BOTH,Canvas


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
    

