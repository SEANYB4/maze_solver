from tkinter import Tk, BOTH, Canvas
from line import Line
from point import Point
from cell import Cell
from maze import Maze
from window import Window


def main():
    # Define window
    win = Window(800, 600)

    # Create maze
    maze = Maze(20, 20, 10, 10, 30, 30, win)
    maze.create_cells()
    maze.break_walls_r(0, 0)
    maze.reset_cells_visited()
    maze.break_entrance_and_exit()



    # redraw the canvas in a loop
    win.wait_for_close()


main()