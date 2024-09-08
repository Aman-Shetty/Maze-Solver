from src.graphics import Line, Point

class Cell:
    def __init__(self, window=None, visited=False) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._window = window
        self._visited = visited

    def draw(self, x1, y1, x2, y2) -> None:
        if self._window is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._window.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._window.draw_line(line, "white")

        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._window.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._window.draw_line(line, "white")

        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._window.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._window.draw_line(line, "white")

        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._window.draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._window.draw_line(line, "white")

    def draw_move(self, to_cell, undo=False) -> None:
        mid_length = abs(self._x2 - self._x1) // 2
        x_center = mid_length + self._x1
        y_center = mid_length + self._y1

        mid_length2 = abs(to_cell._x2 - to_cell._x1) // 2
        x_center2 = mid_length2 + to_cell._x1
        y_center2 = mid_length2 + to_cell._y1

        fill_color = "red"
        if undo:
            fill_color = "grey"

        line = Line(Point(x_center, y_center), Point(x_center2, y_center2))
        self._window.draw_line(line, fill_color)
