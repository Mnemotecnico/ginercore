#!/usr/local/bin/python
from tkinter import *

class Search(Frame):
    """
    Clase para la busqueda de productos

    """

    def __init__(self, master=None):
        self.width = 85
        super().__init__(master)

        # Instanciar el boton y la entrada
        self.Boton = Button(self, text='Buscar', width=7)
        self.Entrada = Entry(self, width=85)

        # Métodos bind
        #self.Boton.bind('<Button-1>', self.eventHandler)
        #self.Entrada.bind('<KeyPress>', self.eventHandler)

        # Posicionamiento de los widget de la clase
        self.Entrada.grid(row=0, column=0, padx=4, pady=4)
        self.Boton.grid(row=0, column=1, padx=4, pady=4)
        self.grid()

    def getDATA(self):
        """
        :return: Retorna el contenido del widget Entry
        """
        return self.Entrada.get()


if __name__ == '__main__':
    aa = Tk()
    aa.title('Cuadro de búsqueda')
    m = Search(aa)
    aa.mainloop()
