import unittest
from graphics import Cell, Line, Maze, Point, Window


def main():
    #create window
    WIDTH = 800
    HEIGHT = 600
    modifier = 4
    win = Window(WIDTH, HEIGHT)
    num_rows = HEIGHT//modifier
    num_cols = WIDTH//modifier
    size_x, size_y = modifier,modifier
    test = Maze(0,0,num_rows,num_cols,size_x,size_y,win)
    print(test.solve())
    win.wait_for_close()
main()