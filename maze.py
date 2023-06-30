from cell import Cell
from point import Point
import time
import random

class Maze:

    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
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
        for i in range(0, self.num_cols+1):
            self.cells.append([])
            for j in range(0, self.num_rows+1):
                self.cells[i].append(Cell(self.win))
                #self.draw_cell(i, j)

        
    def draw_cell(self, i, j):
        x = self.x1 + i*self.cell_size_x
        y = self.y1 + j*self.cell_size_y
        point_1 = Point(x, y)
        point_2 = Point(x+self.cell_size_x, y+self.cell_size_y)
        self.cells[i][j].draw(point_1, point_2)
        self.animate()

    def animate(self):
        self.win.redraw()
        time.sleep(0.05)


    def break_entrance_and_exit(self):
        self.cells[0][0].has_left_wall = False
        self.cells[self.num_cols][self.num_rows].has_right_wall = False

        for i in range(0, self.num_cols+1):
            for j in range(0, self.num_rows+1):
                self.draw_cell(i, j)

    def break_walls_r(self, i, j):
        cell = self.cells[i][j]
        cell.visited = True
        left_cell = None
        right_cell = None
        above_cell = None
        bottom_cell = None
        try:
            left_cell = self.cells[i-1][j]
        except:
            pass
        try:
            right_cell = self.cells[i+1][j]
        except:
            pass
        try:
            above_cell = self.cells[i][j-1]
        except:
            pass
        try:
            bottom_cell = self.cells[i][j+1]
        except:
            pass
        
        while True:
            coords = []
            
            if (left_cell is not None) and (left_cell.visited == False):
                coords.append((i-1, j, 'left'))
            if (right_cell is not None) and (right_cell.visited == False):
                coords.append((i+1, j, 'right'))
            if (above_cell is not None) and (above_cell.visited == False):
                coords.append((i, j-1, 'above'))
            if (bottom_cell is not None) and (bottom_cell.visited == False):
                coords.append((i, j+1, 'below'))

            if len(coords) == 0:
                return
        
            else: 
                index = random.randrange(0, len(coords))
                cell_2 = self.cells[coords[index][0]][coords[index][1]]
                direction = coords[index][2]

                if direction == 'left':
                    cell.has_left_wall = False
                    cell_2.has_right_wall = False

                elif direction == 'right':
                    cell.has_right_wall = False
                    cell_2.has_left_wall = False

                elif direction == 'above':
                    cell.has_top_wall = False
                    cell_2.has_bottom_wall = False

                elif direction == 'below':
                    cell.has_bottom_wall = False
                    cell_2.has_top_wall = False

                self.break_walls_r(coords[index][0], coords[index][1])
