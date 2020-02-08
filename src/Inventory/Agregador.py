import tkinter

import src.Data
import keys

from tkinter import *
from tkinter import messagebox

class Inventory(Frame):
    def __init__(self, master = None):
        super().__init__(master)

        self.rowHead()

        self.conectorObjectSQL = None

    def set_conectorSQL(self, conectorObjact):
        self.conectorObjectSQL = conectorObjact

    def AddProductToInventory(self, event):
        name = self.nameEntry.get()
        stock = self.stockEntry.get()
        pvp = self.pvpEntry.get()
        pva = self.pvaEntry.get()
        ubi = self.ubiEntry.get()
        datos = (name, stock, pvp, pva, ubi)
        if name != '' and stock != '' and pvp != '' and pva != '' and ubi != '':
            if messagebox.askquestion('Advertencia', 'Esta acción modifica la base de datos.\n¿Estás seguro?'):
                try:
                    self.conectorObjectSQL.AddToInventary(datos)
                    self.nameEntry.delete(0, 'end')
                    self.stockEntry.delete(0, 'end')
                    self.pvaEntry.delete(0, 'end')
                    self.pvpEntry.delete(0, 'end')
                    self.ubiEntry.delete(0, 'end')
                except: messagebox.showerror('Error', 'No se pudo realizar la acción.')
        else:
            messagebox.showerror('Error', 'Alguno de los campos está vacío.')

    def rowHead(self):
        FrameHead = Frame(self)
        FrameHead.grid()


        self.nameHead = Label(FrameHead, text = "Nombre del producto")
        self.stockHead = Label(FrameHead, text = "Cantidad")
        self.pvpHead = Label(FrameHead, text = 'PVP')
        self.pvaHead = Label(FrameHead, text = 'PVA')
        self.ubiHead = Label(FrameHead, text = 'Ubicación')

        self.nameHead.grid(row = 0, column = 0, padx = 60, pady = 5)
        self.stockHead.grid(row=0, column=1, padx=10, pady=5)
        self.pvpHead.grid(row=0, column=2, padx=10, pady=5)
        self.pvaHead.grid(row=0, column=3, padx=10, pady=5)
        self.ubiHead.grid(row=0, column=4, padx=60, pady=5)

        self.nameEntry = Entry(FrameHead, width = 60)
        self.stockEntry = Entry(FrameHead, width = 10)
        self.pvpEntry = Entry(FrameHead, width = 10)
        self.pvaEntry = Entry(FrameHead, width = 10)
        self.ubiEntry = Entry(FrameHead, width = 60)

        self.nameEntry.grid(row = 1, column = 0, padx = 5)
        self.stockEntry.grid(row = 1, column = 1, padx = 5)
        self.pvpEntry.grid(row = 1, column = 2, padx = 5)
        self.pvaEntry.grid(row = 1, column = 3, padx = 5)
        self.ubiEntry.grid(row = 1, column = 4, padx = 5)

        self.buttonRegister = Button(self, text = 'Realizar registro', width = 40, relief = 'groove')
        self.buttonRegister.bind('<ButtonRelease-1>', self.AddProductToInventory)
        self.buttonRegister.grid(row = 1, column = 0, padx = 5, pady = 10)




if __name__ == '__main__':
    conector = src.Data.Ginerdata(keys.USER, keys.HOST, keys.PASS, keys.DATABASE)
    a = Tk()
    b = Inventory(a)
    b.grid()
    b.set_conectorSQL(conector)

    a.mainloop()