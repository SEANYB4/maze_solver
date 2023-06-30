from line import Line
from point import Point


class Cell:

    def __init__(self, win):

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


