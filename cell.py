from line import Line
from point import Point


class Cell:

    def __init__(self, win=None):

        self.win = win
        self.canvas = win.canvas
        self.x1 = None
        self.y1 = None
        self.x2 = None
        self.y2 = None
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False


    def draw(self, point_1, point_2):
        self.x1 = point_1.x
        self.y1 = point_1.y
        self.x2 = point_2.x
        self.y2 = point_2.y

        point_3 = Point(self.x2, self.y1)
        point_4 = Point(self.x1, self.y2)

        if self.has_left_wall:
            left_wall = Line(point_1, point_4)
            left_wall.draw(self.canvas, 'red')

        if self.has_right_wall:
            right_wall = Line(point_3, point_2)
            right_wall.draw(self.canvas, 'red')

        if self.has_top_wall:
            right_wall = Line(point_1, point_3)
            right_wall.draw(self.canvas, 'red')

        if self.has_bottom_wall:
            right_wall = Line(point_4, point_2)
            right_wall.draw(self.canvas, 'red')



    def draw_move(self, to_cell, undo=False):

        start_x = self.x2 - ((self.x2 - self.x1)/2)
        start_y = self.y2 - ((self.y2 - self.y1)/2)
        point_1 = Point(start_x, start_y)

        end_x = to_cell.x2 - ((to_cell.x2 - to_cell.x1)/2)
        end_y = to_cell.y2 - ((to_cell.y2 - to_cell.y1)/2)
        point_2 = Point(end_x, end_y)

        move = Line(point_1, point_2)
        if undo == True:
            color = 'gray'
        else:
            color = 'blue'

        move.draw(self.canvas, color)

