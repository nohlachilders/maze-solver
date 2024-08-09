from maze import *

def test_lines(win):
    win.draw_line(Line(Point(100,100),Point(200,200)),"black")
    win.draw_line(Line(Point(300,100),Point(700,100)),"red")


def test_cells(win):
    cell_size = 30
    coords = [
            [10 + 3*x*cell_size for x in range(0,10)],
            [10 + 3*y*cell_size for y in range(0,10)]
            ]

    cells = []
    for x in coords[0]:
        for y in coords[1]:
            cells.append(Cell(x,y,x+cell_size,y+cell_size,win))

    walls = [(True,True,True,False),
             (True,True,True,False),
             (True,True,False,True),
             (True,True,False,False),
             (False,True,True,False),
             (True,False,True,True),]

    for i in range(0,len(walls)):
        cells[i].has_top_wall = walls[i][0]
        cells[i].has_bottom_wall = walls[i][1]
        cells[i].has_left_wall = walls[i][2]
        cells[i].has_right_wall = walls[i][3]


    for cell in cells:
        cell.draw()

    cells[0].draw_move(cells[1])
    cells[15].draw_move(cells[3], True)

