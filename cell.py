class Cell:

    def __init__(self, win, point_1, point_2):

        self.__win = win
        self.__x1 = point_1.x
        self.__y1 = point_1.y
        self.__x2 = point_2.x
        self.__y2 = point_2.y
        has_left_wall = True
        has_right_wall = True
        has_top_wall = True
        has_bottom_wall = True


    def draw(self):

        