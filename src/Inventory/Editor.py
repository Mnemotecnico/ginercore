import tkinter
import src.Table
import src.Data
import keys
from tkinter import messagebox


class Editor(src.Table.Tabla):
    def __init__(self, master=None):
        self.Frame = tkinter.Frame(master)
        super().__init__(self.Frame)


        self.ObjectSearch = self.createObjetSearch(self.Frame)
        self.ObjectSearch.grid(row = 0, column = 0)

        super().grid(row = 1, column = 0)

        self.ObjectEditButton = self.createButtonEdit(self.Frame)
        self.ObjectEditButton.grid(row=2, column=0, padx = 5, pady = 5)

        self.EditTable = self.createTableEditContent(self.Frame)
        self.EditTable.grid(row = 3, column = 0)

        self.bUpdate = self.createButtonUpdate(self.Frame)
        self.bUpdate.grid(row = 4, column = 0)


        # Variables importantes
        self.sqlObject = None


        self.createTB(
            {
                'head': 'ID',
                'anchor': 's',
                'width': 75,

            },
            {
                'head': 'Nombre del producto',
                'anchor': 'w',
                'width': 300,

            },
            {
                'head': 'Código de barras',
                'anchor': 's',
                'width': 150,
            },
            {
                'head': 'Existencias',
                'anchor': 's',
                'width': 75,
            },
            {
                'head': 'PVA',
                'anchor': 's',
                'width': 45,
            },
            {
                'head': 'PVP',
                'anchor': 's',
                'width': 45,
            },
            {
                'head': 'Ubicación',
                'anchor': 's',
                'width': 300,
            }
        )

    def set_sqlObject(self, sqlObject):
        self.sqlObject = sqlObject

    def createObjetSearch(self, frame):
        self.FrameObjectSeach = tkinter.Frame(frame)

        self.EntrySearchToEdit = tkinter.Entry(self.FrameObjectSeach, width = 100)
        self.EntrySearchToEdit.bind('<KeyPress>', self.evenHandlerSearchEntry)
        self.EntrySearchToEdit.grid(row = 0, column = 0)

        self.BotonSearchToEdit = tkinter.Button(self.FrameObjectSeach, text='Buscar', relief = tkinter.GROOVE)
        self.BotonSearchToEdit.bind('<ButtonRelease-1>', self.evenHandlerSearchEntry)
        self.BotonSearchToEdit.grid(row=0, column=1, padx = 5, pady = 5)


        return self.FrameObjectSeach

    def createButtonEdit(self, frame):
        self.ButtonEditFrame = tkinter.Frame(frame)
        self.BotonEdit = tkinter.Button(self.ButtonEditFrame, width = 40, text = 'Editar fila', relief = 'groove')
        self.BotonEdit.bind('<ButtonRelease-1>', self.evenHandlerButtonEdit)
        self.BotonEdit.grid(pady = 5)

        return self.ButtonEditFrame

    def createButtonUpdate(self, frame):
        self.ButtonUpdateFrame = tkinter.Frame(frame)
        self.BotonUpdate = tkinter.Button(self.ButtonUpdateFrame, width = 40, text = 'Actualizar', relief = 'groove')
        self.BotonUpdate.bind('<ButtonRelease-1>', self.evenHandlerButtonUpdate)
        self.BotonUpdate.grid(pady = 15)

        return self.ButtonUpdateFrame

    def createTableEditContent(self, frame):
        FrameHead = tkinter.Frame(frame)

        self.productID = tkinter.Label(FrameHead, text="ID")
        self.nombreProduct = tkinter.Label(FrameHead, text="Nombre del producto")
        self.barrasCode = tkinter.Label(FrameHead, text='Código de barras')
        self.stock = tkinter.Label(FrameHead, text='Existencias')
        self.pricePVA = tkinter.Label(FrameHead, text='PVA')
        self.pricePVP = tkinter.Label(FrameHead, text='PVP')
        self.ubihead = tkinter.Label(FrameHead, text='Ubicación')

        self.productID.grid(row=0, column=0, padx=20, pady=5)
        self.nombreProduct.grid(row=0, column=1, padx=60, pady=5)
        self.barrasCode.grid(row=0, column=2, padx=20, pady=5)
        self.stock.grid(row=0, column=3, padx=10, pady=5)
        self.pricePVA.grid(row=0, column=4, padx=10, pady=5)
        self.pricePVP.grid(row=0, column=5, padx=10, pady=5)
        self.ubihead.grid(row=0, column=6, padx=60, pady=5)

        self.identry = tkinter.Entry(FrameHead, width=10, state='disabled')
        self.nameEntry = tkinter.Entry(FrameHead, width=40, state='disabled')
        self.bcodeEntry = tkinter.Entry(FrameHead, width=20, state='disabled')
        self.stockEntry = tkinter.Entry(FrameHead, width=15, state='disabled')
        self.pvaEntry = tkinter.Entry(FrameHead, width=6, state='disabled')
        self.pvpEntry = tkinter.Entry(FrameHead, width=6, state='disabled')
        self.ubiEntry = tkinter.Entry(FrameHead, width=40, state='disabled')

        self.identry.grid(row=1, column=0, padx=2)
        self.nameEntry.grid(row=1, column=1, padx=2)
        self.bcodeEntry.grid(row=1, column=2, padx=2)
        self.stockEntry.grid(row=1, column=3, padx=2)
        self.pvaEntry.grid(row=1, column=4, padx=2)
        self.pvpEntry.grid(row=1, column=5, padx=2)
        self.ubiEntry.grid(row=1, column=6, padx=2)

        return FrameHead

    def evenHandlerButtonUpdate(self, event):
        if self.nameEntry.get() != '' and self.stockEntry.get() != '' and self.pvaEntry.get() != '' and self.pvpEntry.get() != '':
            allow = messagebox.askquestion('Advertencia', 'Esta acción modificará la base de datos.\n¿Estás seguro?')
            if allow:
                barras = self.bcodeEntry.get()
                nombre = self.nameEntry.get()
                stock = self.stockEntry.get()
                pva = self.pvaEntry.get()
                pvp = self.pvpEntry.get()
                ubi = self.ubiEntry.get()
                producID = self.identry.get()

                row = (barras, nombre, stock, pva, pvp, ubi, producID)
                if self.sqlObject.UpdateInventory(row):
                    self.bcodeEntry.delete(0, 'end')
                    self.nameEntry.delete(0, 'end')
                    self.stockEntry.delete(0, 'end')
                    self.pvaEntry.delete(0, 'end')
                    self.pvpEntry.delete(0, 'end')
                    self.ubiEntry.delete(0, 'end')

                    self.identry.config(state = 'normal')
                    self.identry.delete(0, 'end')

                    self.identry.config(state = 'disabled')
                    self.bcodeEntry.config(state = 'disabled')
                    self.nameEntry.config(state = 'disabled')
                    self.stockEntry.config(state = 'disabled')
                    self.pvaEntry.config(state = 'disabled')
                    self.pvpEntry.config(state = 'disabled')
                    self.ubiEntry.config(state = 'disabled')

                    self.Treeview.delete(*self.Treeview.get_children())
                    self.EntrySearchToEdit.delete(0, 'end')




        else:
            messagebox.showerror('Error', 'No se realizaron modificaciones.')


    def evenHandlerButtonEdit(self, event):
        Item = self.Treeview.selection()
        if Item != ():
            rowData = self.Treeview.item(Item)
            if rowData['values'][1] == 'None':
                rowData['values'][1] = ''


            self.identry.config(state = 'normal')
            self.identry.insert(0, rowData['text'])
            self.identry.config(state='disabled')

            self.nameEntry.config(state='normal')
            self.nameEntry.insert(0, rowData['values'][0])

            self.bcodeEntry.config(state='normal')
            self.bcodeEntry.insert(0, rowData['values'][1])

            self.stockEntry.config(state = 'normal')
            self.stockEntry.insert(0, rowData['values'][2])

            self.pvaEntry.config(state = 'normal')
            self.pvaEntry.insert(0, rowData['values'][3])

            self.pvpEntry.config(state='normal')
            self.pvpEntry.insert(0, rowData['values'][4])

            self.ubiEntry.config(state='normal')
            self.ubiEntry.insert(0, rowData['values'][5])
        else: messagebox.showerror('Error', 'No has selccionado nada.')


    def evenHandlerSearchEntry(self, event):
        input = self.EntrySearchToEdit.get()
        datos = self.sqlObject.buscarProductos(input)
        productos = []
        if datos is not None:
            for d in datos:
                productos.append((d[0], d[2], d[1], d[3], d[4], d[5], d[6]))


        self.insertDATA(productos, clear=True)







if __name__ == '__main__':
    window = tkinter.Tk()
    a = Editor(window)
    b = src.Data.Ginerdata(keys.USER, keys.HOST, keys.PASS, keys.DATABASE)
    a.set_sqlObject(b)
    a.Frame.grid()

    window.mainloop()