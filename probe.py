from tkinter import *
import src.uTable
import src.uSearch
import src.uData


def main():
    conector = src.uData.Ginerdata(host='216.231.129.35', user='idemself_ginercor', password='itg#2]/pln%8dk@n',
                                   database='idemself_test')

    window = Tk()
    window.title('Sistema de control administrativo')
    TableFrame = Frame(window)  # Frame de la busqueda de productos (entry, treeview y button)
    CestaFrame = Frame(window)  # Frame de la cesta de productos y calculadora
    TableFrame.grid()
    CestaFrame.grid(row=0, column=1)

    # <--- *** TableFrame *** ---> #
    SearchTabP = src.uSearch.Search(TableFrame)  # Entrada de busqueda
    TabProductos = src.uTable.Tabla(TableFrame, height=15)  # Tabla de productos de busqueda
    TabProductos.createTB(  # Se configura la forma de la tabla
        {'head': 'Nombre del producto', 'anchor': 'w', 'width': 450},
        {'head': 'Precio', 'width': 50, 'anchor': 'center'},
        {'head': 'Existencias', 'width': 75, 'anchor': 'center'}
    )
    AddCesta = Button(window, text='Añadir a la cesta')   # Este boton será el añadir a la cesta de la tabla de busqueda
    AddCesta.grid(row=1, column=0)

    def retrieveTabP(event):  # Esta funcion será el EventHandler de SearchTabP
        inputData = SearchTabP.getDATA()
        pData = conector.buscarProductos(inputData)
        rowsProducts = []
        if pData is not None:
            for rowcomplet in pData:
                rowsProducts.append([rowcomplet[2], rowcomplet[5], rowcomplet[3]])
        TabProductos.insertDATA(rowsProducts, clear=True)

    SearchTabP.Boton.bind('<Button-1>', retrieveTabP)
    SearchTabP.Entrada.bind('<Return>', retrieveTabP)

    # <--- *** CestaFrame *** ---> #
    CestaTable = src.uTable.Tabla(CestaFrame, height=5)
    CestaTable.createTB(
        {'head': 'Producto', 'anchor': 'w', 'width': 150},
        {'head': 'Precio', 'anchor': 'center', 'width': 50},
        {'head': 'Cantidad', 'anchor': 'center', 'width': 75}
    )

    window.mainloop()


if __name__ == '__main__':
    main()
