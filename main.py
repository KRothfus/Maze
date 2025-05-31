from graphics import Cell, Line, Point, Window


def main():
    #create window
    win = Window(800, 600)
    #create a couple of points
    p1 = Point(400, 300)
    p2 = Point(400, 100)
    #draw a green line with those points
    line = Line(p1,p2)
    win.draw_line(line, 'green')
    #create 1st cell and draw it
    cell1 = Cell(win)
    cell1.has_right_wall = False
    cell1.draw(10,10,200,200)
    #create 2nd cell and draw it with no bottom wall
    cell2 = Cell(win)
    cell2.has_left_wall = False
    cell2.has_right_wall = False
    cell2.draw(200,10,400,200)
    cell1.draw_move(cell2)
    #create 3rd cell and draw it with only top and bottom wall
    cell3 = Cell(win)
    cell3.has_bottom_wall = False
    cell3.has_left_wall = False
    cell3.draw(400,10,600,200)
    cell2.draw_move(cell3)
    win.wait_for_close()

main()