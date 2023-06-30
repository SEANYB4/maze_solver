class Cell:

    def __init__(self, win, point_1, point_2):

        self.__win = win
        self.__x1 = None
        self.__y1 = None
        self.__x2 = None
        self.__y2 = None
        has_left_wall = True
        has_right_wall = True
        has_top_wall = True
        has_bottom_wall = True


    def draw(self):

