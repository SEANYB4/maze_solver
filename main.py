from tkinter import Tk, BOTH, Canvas
from line import Line
from point import Point
from cell import Cell
class Window:

    def __init__(self, width, height):

        self.root = Tk()
        self.root.title = 'Maze Solver'
        self.canvas = Canvas(self.root, height=height, width=width)
        self.canvas.pack()
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)


def main():
    # Define window
    win = Window(800, 600)

    #Draw a cell
    point_1 = Point(20, 40)
    point_2 = Point(60, 80)
    cell_1 = Cell(win)
    cell_1.draw(point_1, point_2)

    #Draw another cell
    point_3 = Point(200, 300)
    point_4 = Point(240, 340)
    cell_2 = Cell(win)
    cell_2.draw(point_3, point_4)


    # draw move between cells
    cell_1.draw_move(cell_2)


    # redraw the canvas in a loop
    win.wait_for_close()


main()