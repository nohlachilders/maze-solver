from maze import *
from drawingtests import *

def main():
    win = Window(800, 600)
    #test_cells(win)
    maze = Maze(0,0,10,10,30,30,win)
    win.wait_for_close()

main()
