from tkinter import Tk, BOTH, Canvas

class Window():

    def __init__(self, width, height):
        self.root_widget = Tk()
        self.root_widget.title = "Root Widget"
        self.canvas = Canvas(height = height, width = width)
        self.canvas.pack()
        self.running = False

