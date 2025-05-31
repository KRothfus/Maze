from graphics import Line, Point, Window


def main():
    win = Window(800, 600)
    p1 = Point(400, 300)
    p2 = Point(400, 100)
    line = Line(p1,p2)
    win.draw_line(line, 'green')
    win.wait_for_close()

main()