#!/usr/local/bin/python
from tkinter import *
from tkinter.ttk import *


class Tabla(Frame):
    """
    Esta clase permite crear una tabla con encabezados personalizados
    """

    def __init__(self, master=None, height=10):
        super().__init__(master)
        self.Treeview = Treeview(self, height=height)  # Instancia de Treeview para trabajar como una propiedad nativa de la clase
        self.grid()

        self.Scrollbar = Scrollbar(self, orient="vertical", command=self.Treeview.yview)
        self.Scrollbar.pack(side='right', fill='y')

    def createTB(self, *args):
        '''
        :param args: Cadenas de texto que representan el encabezado de la columna o diccionarios {head:value, width:value, anchor:value}
        :return: No tiene retorno
        '''

        encabezados = []  # Lista de diccionarios
        for element in args:
            if type(element) == str:
                encabezados.append({'head': element})
            elif type(element) == dict:
                encabezados.append(element)

        titulos = []  # Lista con cadenas de texto para los encabezados de la tabla
        widths = []  # Lista con enteros sobre el ancho de la columna (si no existe el valor tendrá None)
        anchors = []  # Lista con enteros sobre el sticky de la columna (si no existe el valor tendrá None)
        for element in encabezados:  # Fracciona el diccionario a en listas (titulos, widths, anchors)
            titulos.append(element['head'])
            try:
                widths.append(element['width'])
            except:
                widths.append(None)

            try:
                anchors.append(element['anchor'])
            except:
                anchors.append(None)

        self.Treeview['column'] = titulos[1:]  # Asigna los titulos y datos a los encabezados de la tabla
        for element in range(len(titulos)):
            mode = 0  # 0: Sin anchor ni width, 1: Solo width, 2: Just anchor, 3: Anchor y width
            if widths[element] is not None:
                mode = 1
                if anchors[element] is not None:
                    mode = 3
            else:
                if anchors[element] is not None:
                    mode = 2

            if element == 0:  # Este condicional es únicamente para el encabezado padre #0

                if mode == 0:
                    self.Treeview.heading("#0", text=titulos[element])
                elif mode == 1:
                    self.Treeview.heading("#0", text=titulos[element])
                    self.Treeview.column('#0', width=widths[element])
                elif mode == 2:
                    self.Treeview.heading("#0", text=titulos[element], anchor=anchors[element])
                elif mode == 3:
                    self.Treeview.heading("#0", text=titulos[element], anchor=anchors[element])
                    self.Treeview.column('#0', width=widths[element])
            else:  # Este bloque se ejecuta los encabezados no principales

                if mode == 0:
                    self.Treeview.heading(titulos[element], text=titulos[element])
                elif mode == 1:
                    self.Treeview.heading(titulos[element], text=titulos[element])
                    self.Treeview.column(titulos[element], width=widths[element])
                elif mode == 2:
                    self.Treeview.heading(titulos[element], text=titulos[element], anchor=anchors[element])
                elif mode == 3:
                    self.Treeview.heading(titulos[element], text=titulos[element], anchor=anchors[element])
                    self.Treeview.column(titulos[element], width=widths[element])

        self.Treeview.pack(side="left")

        # Configuración del Scrollbar
        self.Treeview.config(yscrollcommand=self.Scrollbar.set)

    def insertDATA(self, content, clear=False):
        """

        :param content: Lista de tuplas. Cada tupla debe tener los datos de una fila completa DE LA TABLA.
        :param clear: Meter <True> limpiará la tabla de los datos que contenga (en caso de que hayan). False lo ignora.
        :return: sin retorno.
        """
        if clear:
            self.Treeview.delete(*self.Treeview.get_children())

        if len(content) == 0 or len(content[0]) == 0:
            pass
        else:
            for data in content:
                self.Treeview.insert('', 'end', text=data[0], values=data[1:])

    def getSELECTION(self):
        """
        Este método entregará la fila selecionada cuando es llamado
        :return: Datos (en orden) de la fila seleccionada
        """

        # Diccionario con la información de la fila {'text': 1, 'image': '', 'values': ['nmas'], 'open': 0, 'tags': ''}
        contentT = self.Treeview.item(self.Treeview.selection())
        datos = [contentT['text']] + contentT['values']
        return datos


if __name__ == '__main__':
    window = Tk()
    window.title('Hola')
    a = Tabla(master=window)
    a.createTB({'head': 'Nombre del producto', 'anchor': 'w', 'width': 500}, {'head': 'Precio', 'width': 45})
    a.insertDATA([(1, 'nmas'), ('cpsad', 55.5)], clear=True)
    window.mainloop()
