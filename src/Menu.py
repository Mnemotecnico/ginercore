from tkinter import *

class SpecialMenu(Menu):
    def __init__(self, master = None):
        super().__init__(master)

        self.filename = Menu(self, tearoff = 0)
        self.filename.add_command(label="En construcción...")
        self.add_cascade(label = "Estado", menu = self.filename)
        self.add_cascade(label="Modificaciones", menu=self.filename)

if __name__ == '__main__':

    window = Tk()
    menu = SpecialMenu(window)

    window.config(menu=menu)
    window.mainloop()