from cell import Cell
import time
import random

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []

    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self.win))
            self._cells.append(col_cells)

        for i in range(self._num_cols):
            for j in range(self._num_cells):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
       cell_x1 = self.x1 + (self.cell_size_x * i)
       cell_y1 = self.y1 + (self.cell_size_y * j)
       cell_x2 = cell_x1 + self.cell_size_x
       cell_y2 = cell_y1 + self.cell_size_y
       self._cells[i][j].draw(cell_x1, cell_y1, cell_x2, cell_y2)
       self._animate()

    def _animate(self):
        if self._win is None:
            return
        self.win.redraw()
        time.sleep(0.05)
       


