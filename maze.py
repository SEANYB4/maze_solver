from cell import Cell
from point import Point
import time

class Maze:

    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.cells = []
        self.create_cells()

    def create_cells(self):
        for i in range(0, self.num_cols):
            self.cells.append([])
            for j in range(0, self.num_rows):
                self.cells[i].append(Cell(self.win))
                cell = self.cells[i]
                self.draw_cell(self, i, j, cell)

    def draw_cell(self, i, j, cell):
        x = self.x1 + i*self.cell_size_x
        y = self.y1 + j*self.cell_size_y
        point_1 = Point(x, y)
        point_2 = Point(x+self.cell_size_x, y+self.cell_size_y)
        cell.draw(point_1, point_2)
        self.animate()

    def animate(self):
        self.win.redraw()
        time.sleep(0.05)
