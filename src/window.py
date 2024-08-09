from tkinter import Tk, BOTH, Canvas

class Point:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y

class Line:
    def __init__(self, a:Point, b:Point):
        self.a = a
        self.b = b

    def draw(self, canvas:Canvas, fill_color:str):
        canvas.create_line(
                self.a.x, self.a.y, self.b.x, self.b.y, fill=fill_color, width=2
                )

class Window:
    def __init__(self, width:int, height:int):
        self.__root = Tk()
        self.__root.title = "something"

        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack()
        self.__is_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update()
        self.__root.update_idletasks()

    def wait_for_close(self):
        self.__is_running = True
        while self.__is_running == True:
            self.redraw()
    
    def close(self):
        self.__is_running = False

    def draw_line(self, line:Line, fill_color:str):
        line.draw(self.__canvas, fill_color)

