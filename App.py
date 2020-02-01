from tkinter import *
from tkinter import messagebox
import src.Table
import src.Search
import src.Data
import src.Menu
import src.CuentaPago

# Non direction
def main():
    conector = src.Data.Ginerdata(host='localhost', user='root', password='',
                                  database='test')

    # Construcción de la ventana principal & widgets
    window = Tk()
    window.title('Sistema de control administrativo')

    # < Instancias de Frames > #
    TableFrame = Frame(window)  # Frame de la busqueda de productos (entry, treeview y button)
    CestaFrame = Frame(window)  # Frame de la cesta de productos y calculadora
    TableFrame.grid()
    CestaFrame.grid(row=0, column=1)


    # <--- *** TableFrame *** ---> #
    # Esta funcion será el EventHandler de SearchTabP
    def retrieveTabP(event):
        inputData = SearchTabP.getDATA()
        pData = conector.buscarProductos(inputData)
        rowsProducts = []
        if pData is not None:
            for rowcomplet in pData:
                rowsProducts.append([rowcomplet[2], rowcomplet[5], rowcomplet[3]])
        TabProductos.insertDATA(rowsProducts, clear=True)


    # Esta función será un ResponseHandler de TableFrame
    def submit_cest(event):
        try:
            focus_select = TabProductos.Treeview.item(TabProductos.Treeview.selection())
            focus_select = [focus_select['text'], float(focus_select['values'][0]), int(entry_cant.get())]
            CestaTable.insertDATA([tuple(focus_select)], clear=False)
            TabProductos.Treeview.selection_remove(TabProductos.Treeview.selection())
            entry_cant.delete(0, 'end')
            SearchTabP.Entrada.delete(0, 'end')
        except:
            messagebox.showerror('Oye, tranquilo viejo', 'No se puede añadir eso.')

    SearchTabP = src.Search.Search(TableFrame)  # Entrada de busqueda
    TabProductos = src.Table.Tabla(TableFrame, height=15)  # Tabla de productos de busqueda
    # TabProductos.Treeview.bind('<<TreeviewSelect>>', getfocus) # Evento de selección de productos en inventario

    TabProductos.createTB(  # Se configura la forma de la tabla
        {'head': 'Nombre del producto', 'anchor': 'w', 'width': 450},
        {'head': 'Precio', 'width': 50, 'anchor': 'center'},
        {'head': 'Existencias', 'width': 75, 'anchor': 'center'}
    )

    entry_cant = Entry(SearchTabP, width=4)
    entry_cant.grid(row=0, column=2, padx=3)

    AddCesta = Button(SearchTabP, text='Agregar', relief = GROOVE)  # Este boton será el añadir a la cesta de la tabla de busqueda
    AddCesta.bind('<ButtonRelease-1>', submit_cest)
    AddCesta.grid(row=0, column=3)

    SearchTabP.Boton.bind('<Button-1>', retrieveTabP)
    SearchTabP.Entrada.bind('<KeyPress>', retrieveTabP)
    SearchTabP.Entrada.bind('<Return>', retrieveTabP)

    # <--- *** CestaFrame *** ---> #

    # Función EventHandler para eliminar items del objeto cesta
    def del_icesta(event):
        try:
            if CestaTable.Treeview.selection() != ():
                for item in CestaTable.Treeview.selection():
                    CestaTable.Treeview.delete(item)
            else:
                messagebox.showerror('Error', 'No has seleccionado nada')
        except:
            messagebox.showerror('Error', 'No se realizó la acción')

    # Frame de la cuenta
    cuenta = src.CuentaPago.CuentaPago(CestaFrame)

    # Frame de la cesta de compra
    CestaTable = src.Table.Tabla(CestaFrame, height=5)
    CestaTable.createTB(
        {'head': 'Producto', 'anchor': 'w', 'width': 150},
        {'head': 'Precio', 'anchor': 'center', 'width': 50},
        {'head': 'Cantidad', 'anchor': 'center', 'width': 75}
    )

    # Botón de borrar elemento de la cesta de compra
    DeleteCesta = Button(CestaFrame, text = "Eliminar de la cesta", relief = GROOVE)
    DeleteCesta.bind('<ButtonRelease-1>', del_icesta)
    DeleteCesta.grid(pady = 5)
























    window.config(menu=src.Menu.SpecialMenu(window))
    window.mainloop()


if __name__ == '__main__':
    main()
