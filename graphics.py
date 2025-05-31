import time
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
    def __init__(self, window=None):
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
        
        if self.has_left_wall and self.__win:
            self.__win.draw_line(Line(Point(self.__x1,self.__y1),Point(self.__x1,self.__y2)),fill_color)
        else:
            self.__win.draw_line(Line(Point(self.__x1,self.__y1),Point(self.__x1,self.__y2)),'white')
        if self.has_right_wall and self.__win:
            self.__win.draw_line(Line(Point(self.__x2,self.__y1),Point(self.__x2,self.__y2)),fill_color)
        else:
            self.__win.draw_line(Line(Point(self.__x2,self.__y1),Point(self.__x2,self.__y2)),'white')
        if self.has_top_wall and self.__win:
            self.__win.draw_line(Line(Point(self.__x1,self.__y1),Point(self.__x2,self.__y1)),fill_color)
        else:
            self.__win.draw_line(Line(Point(self.__x1,self.__y1),Point(self.__x2,self.__y1)),'white')
        if self.has_bottom_wall and self.__win:
            self.__win.draw_line(Line(Point(self.__x1,self.__y2),Point(self.__x2,self.__y2)),fill_color)
        else:
            self.__win.draw_line(Line(Point(self.__x1,self.__y2),Point(self.__x2,self.__y2)),'white')
    
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
        
class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.__cells = []
        self.__create_cells()
    
    def __create_cells(self):
        for i in range(self.num_cols):
            self.__cells.append([])
            for j in range(self.num_rows):
                self.__cells[i].append(Cell(self.win))
                self.__draw_cell(i,j)
    
    def __draw_cell(self, i, j):
        x1 = (self.cell_size_x) * i + self.x1
        y1 = (self.cell_size_y) * j + self.y1
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        self.__cells[i][j].draw(x1,y1,x2,y2)
        self.animate()
    
    def animate(self):
        if self.win != None:
            self.win.redraw()
            time.sleep(.005)
            
    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0,0)
        self.__cells[self.num_rows-1][self.num_cols-1].has_bottom_wall = False
        self.__draw_cell(self.num_rows-1,self.num_cols-1)