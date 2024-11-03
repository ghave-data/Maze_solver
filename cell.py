from draw import Point, Line

class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win
    
    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        top_left = Point(x1, y1)
        bottom_left = Point(x1, y2)
        top_right = Point(x2, y1)
        bottom_right = Point(x2, y2)
        if self.has_left_wall:
            line = Line(top_left, bottom_left)
            self._win.draw_line(line)
        if self.has_right_wall:
            line = Line(top_right, bottom_right)
            self._win.draw_line(line)
        if self.has_top_wall:
            line = Line(top_right, top_left)
            self._win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(bottom_right, bottom_left)
            self._win.draw_line(line)
    
    def draw_move(self, to_cell, undo=False):
        self_center_point = Point((self._x1+self._x2)/2, (self._y1+self._y2)/2)
        to_cell_center_point = Point((to_cell._x1+to_cell._x2)/2, (to_cell._y1+to_cell._y2)/2)
        line = Line(self_center_point, to_cell_center_point)
        fill_color = "red"
        if undo:
            fill_color = "grey"
        self._win.draw_line(line, fill_color)
