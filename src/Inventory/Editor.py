import tkinter
import src.Table


class Editor(src.Table.Tabla):
    def __init__(self, master=None):
        self.Frame = tkinter.Frame(master)
        super().__init__(self.Frame)


        self.ObjectSearch = self.createObjetSearch(self.Frame)
        self.ObjectSearch.grid(row = 0, column = 0)

        super().grid(row = 1, column = 0)


        self.createTB(
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

    def createObjetSearch(self, frame):
        self.FrameObjectSeach = tkinter.Frame(frame)

        self.EntrySearchToEdit = tkinter.Entry(self.FrameObjectSeach, width = 100)
        self.EntrySearchToEdit.grid(row = 0, column = 0)

        self.BotonSearchToEdit = tkinter.Button(self.FrameObjectSeach, text='Buscar', relief = tkinter.GROOVE)
        self.BotonSearchToEdit.grid(row=0, column=1, padx = 5, pady = 5)


        return self.FrameObjectSeach





if __name__ == '__main__':
    window = tkinter.Tk()
    a = Editor(window)
    a.Frame.grid()

    window.mainloop()