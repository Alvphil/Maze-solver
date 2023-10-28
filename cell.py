from graphics import Line, Point

class Cell:
    def __init__(self, win=None,
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
        self.visited = False
        self.__top_left = 0   #top_left.x
        self.__top_right = 0   #bottom_right.x
        self.__bottom_left = 0   #top_left.y
        self.__bottom_right = 0   #bottom_right.y
        self.__win = win

    def draw(self, top_left_point, bottom_right_point):
            if self.__win is None:
                return
            self.__top_left = top_left_point
            self.__bottom_right = bottom_right_point
            self.__top_right = Point(bottom_right_point.x, top_left_point.y)
            self.__bottom_left = Point(top_left_point.x, bottom_right_point.y)
            if self.has_top_wall:
                self.__win.draw_line(Line(self.__top_left, self.__top_right), "black")
            else:
                self.__win.draw_line(Line(self.__top_left, self.__top_right), "white")
            if self.has_right_wall:
                self.__win.draw_line(Line(self.__top_right, self.__bottom_right), "black")
            else:
                self.__win.draw_line(Line(self.__top_right, self.__bottom_right), "white")
            if self.has_bottom_wall:
                self.__win.draw_line(Line(self.__bottom_left, self.__bottom_right), "black")
            else:
                self.__win.draw_line(Line(self.__bottom_left, self.__bottom_right), "white")
            if self.has_left_wall:
                self.__win.draw_line(Line(self.__top_left, self.__bottom_left), "black")
            else:
                self.__win.draw_line(Line(self.__top_left, self.__bottom_left), "white")

    def draw_move(self, to_cell, undo=False):
        if self.__win is None:
            return
        p1 = Point((self.__top_left.x + self.__bottom_right.x) / 2,
                   (self.__top_left.y + self.__bottom_right.y) / 2 )
        p2 = Point((to_cell.__top_left.x + to_cell.__bottom_right.x) / 2,
                   (to_cell.__top_left.y + to_cell.__bottom_right.y) / 2 )
        #self.__win.draw_line(Line(p1, p2), "red")

        fill_color = "red"
        if undo:
            fill_color = "gray"

        # moving left
        if self.__top_left.x > to_cell.__top_left.x:
            line = Line(Point(self.__top_left.x, p1.y), Point(p1.x, p1.y))
            self.__win.draw_line(line, fill_color)
            line = Line(Point(p2.x, p2.y), Point(to_cell.__bottom_right.x, p2.y))
            self.__win.draw_line(line, fill_color)

        # moving right
        elif self.__top_left.x < to_cell.__top_left.x:
            line = Line(Point(p1.x, p1.y), Point(self.__bottom_right.x, p1.y))
            self.__win.draw_line(line, fill_color)
            line = Line(Point(to_cell.__top_left.x, p2.y), Point(p2.x, p2.y))
            self.__win.draw_line(line, fill_color)

        # moving up
        elif self.__top_left.y > to_cell.__top_left.y:
            line = Line(Point(p1.x, p1.y), Point(p1.x, self.__top_left.y))
            self.__win.draw_line(line, fill_color)
            line = Line(Point(p2.x, to_cell.__bottom_right.y), Point(p2.x, p2.y))
            self.__win.draw_line(line, fill_color)

        # moving down
        elif self.__top_left.y < to_cell.__top_left.y:
            line = Line(Point(p1.x, p1.y), Point(p1.x, self.__bottom_right.y))
            self.__win.draw_line(line, fill_color)
            line = Line(Point(p2.x, p2.y), Point(p2.x, to_cell.__top_left.y))
            self.__win.draw_line(line, fill_color)