from window import *
import time
import random

class Cell:
    def __init__(self,
                 x1:int,
                 y1:int,
                 x2:int,
                 y2:int,
                 win:Window = None,):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        self._win = win

        self._visited = False

    def draw(self):
        for pair in [ 
                [self.has_top_wall,Line(Point(self._x1,self._y1),Point(self._x2,self._y1))],
                [self.has_bottom_wall,Line(Point(self._x1,self._y2),Point(self._x2,self._y2))],
                [self.has_left_wall,Line(Point(self._x1,self._y1),Point(self._x1,self._y2))],
                [self.has_right_wall,Line(Point(self._x2,self._y1),Point(self._x2,self._y2))]
                              ]:
            if pair[0]:
                self._win.draw_line(pair[1],"black")
            else:
                self._win.draw_line(pair[1],"white")

    def draw_move(self, to_cell, undo=False):
        center_a = Point((self._x1+self._x2)/2,(self._y1+self._y2)/2)
        center_b = Point((to_cell._x1+to_cell._x2)/2,(to_cell._y1+to_cell._y2)/2)

        match undo:
            case True:
                self._win.draw_line(Line(center_a,center_b),"gray")
            case False: self._win.draw_line(Line(center_a,center_b),"red")

class Maze:
    def __init__(
            self,
            x1:int,
            y1:int,
            num_rows:int,
            num_cols:int,
            cell_size_x:int,
            cell_size_y:int,
            win:Window = None,
            seed:int = None,
            ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed != None:
            self._seed = random.seed(seed)

        self._create_cells()

    def _create_cells(self):
        self._cells = []
        for i in range(0,self._num_cols):
            self._cells.append([])
            for j in range(0,self._num_rows):
                cell = Cell(
                        self._x1+i*self._cell_size_x,
                        self._y1+j*self._cell_size_y,
                        self._x1+(i+1)*self._cell_size_x,
                        self._y1+(j+1)*self._cell_size_y,
                        self._win
                        )
                self._cells[i].append(cell)
        self._break_entrance_and_exit()
        if self._win:
            self._draw_cells()

    def _draw_cells(self):
        for column in self._cells:
            for cell in column:
                cell.draw()
        self._animate()


    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[-1][-1].has_bottom_wall = False
        
    def _break_walls_r(self, i ,j):
        self._cells[i][j]._visited = True
        # TODO the rest of this
