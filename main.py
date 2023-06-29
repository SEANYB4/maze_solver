from tkinter import Tk, BOTH, Canvas
from line import Line
from point import Point
class Window:

    def __init__(self, width, height):

        self.__root = Tk()
        self.__root.title = 'Maze Solver'
        self.__canvas = Canvas(self.__root)
        self.__canvas.pack()
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)


def main():
    win = Window(800, 600)
    point_1 = Point(20, 50)
    point_2 = Point(40, 80)
    line_1 = Line(point_1, point_2)
    win.draw_line(line_1, 'red')


    win.wait_for_close()


main()