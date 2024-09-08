from src.graphics import Window
from src.maze import Maze
import sys

def main() -> None:
    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x -2 * margin) / num_cols
    cell_size_y = (screen_y -2 * margin) / num_rows

    sys.setrecursionlimit(10000)
    window = Window(screen_x, screen_y)
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, window)

    print("maze created")
    is_solvable = maze.solve()
    if not is_solvable:
        print("maze not solvable")
    else:
        print("maze solved")

    window.wait_for_close()


if __name__ == "__main__":
    main()
