from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("RPS")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(self.__root, width=width,
                             height=height, bg="white")
        self.canvas.pack(fill=BOTH, expand=1)
        self.__running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed")

    def close(self):
        self.__running = False


class Ball:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def __repr__(self):
        return f"{self.color} ball with center at ({self.x}, {self.y} and radius of {self.radius}"

    def draw(self, canvas, color):
        left_x = self.x - self.radius
        top_y = self.y - self.radius
        right_x = self.x + self.radius
        bottom_y = self.y + self.radius
        canvas.create_oval(left_x, top_y, right_x, bottom_y, fill=color)
