from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")

    def close(self):
        self.__running = False

    def draw_line(self, Line,fill_color='black'):
        Line.draw(self.__canvas,fill_color)

class Point:
    def __init__(self,x,y):
        self.x = x #x = 0 is the left side of the screen
        self.y = y #y = 0 is the top of the screen
        

class Line:
    def __init__(self, point1, point2):
        self.x1 = point1.x
        self.y1 = point1.y
        self.x2 = point2.x
        self.y2 = point2.y
        
    def draw(self, canvas, fill_color='green'): #fill color is a string like 'black'
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill=fill_color, width=2) #how to get create_line to not be white? it is supposed to accept a canvas as a parameter.

class Cell:
    def __init__(self, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__y1 = -1
        self.__x2 = -1
        self.__y2 = -1
        self.__win = window
    def draw(self, x1, y1, x2, y2, fill_color='black'):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        
        if self.has_left_wall:
            self.__win.draw_line(Line(Point(self.__x1,self.__y1),Point(self.__x1,self.__y2)),fill_color)
        if self.has_right_wall:
            self.__win.draw_line(Line(Point(self.__x2,self.__y1),Point(self.__x2,self.__y2)),fill_color)
        if self.has_top_wall:
            self.__win.draw_line(Line(Point(self.__x1,self.__y1),Point(self.__x2,self.__y1)),fill_color)
        if self.has_bottom_wall:
            self.__win.draw_line(Line(Point(self.__x1,self.__y2),Point(self.__x2,self.__y2)),fill_color)
    
    def _coordinates_set(self):
        if self.__x1 == -1 or self.__x2 == -1 or self.__y1 == -1 or self.__y2 == -1:
            raise Exception('The coordinates are not yet set.')
    
    def draw_move(self, to_cell, undo=False):
        self._coordinates_set()
        to_cell._coordinates_set()
        if undo:
            fill_color = 'gray'
        else:
            fill_color = 'red'
        self_middle_x = ((self.__x2 - self.__x1)/2)+self.__x1
        self_middle_y = ((self.__y2 - self.__y1)/2)+self.__y1
        to_middle_x = ((to_cell.__x2 - to_cell.__x1)/2)+to_cell.__x1
        to_middle_y = ((to_cell.__y2 - to_cell.__y1)/2)+to_cell.__y1
        self.__win.draw_line(Line(Point(self_middle_x,self_middle_y),Point(to_middle_x,to_middle_y)), fill_color)