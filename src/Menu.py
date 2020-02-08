from tkinter import *
import Inventory

class SpecialMenu(Menu):
    def __init__(self, master = None, conector = None):
        super().__init__(master)
        self.conectorObject = conector

        self.filename = Menu(self, tearoff = 0)
        self.inventario = Menu(self, tearoff = 0)



        self.filename.add_command(label="En construcción...")
        self.add_cascade(label = "Estado", menu = self.filename)
        self.add_cascade(label="Modificadores", menu=self.inventario)
        self.add_cascade(label="Panel estocástico", menu=self.filename)

        self.inventario.add_command(label = 'Inventario', command = lambda : Inventory.main(self.conectorObject))

if __name__ == '__main__':

    window = Tk()
    menu = SpecialMenu(window)

    window.config(menu=menu)
    window.mainloop()