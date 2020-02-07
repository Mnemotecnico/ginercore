from tkinter import *
from tkinter import messagebox
import src.Table
import src.Search
import src.Data
import src.Menu
import src.CuentaPago

import keys

# Non direction



def main():
    HOST = keys.HOST
    USER = keys.USER
    PASS = keys.PASS
    DATABASE = keys.DATABASE
    conector = src.Data.Ginerdata(host=HOST, user=USER, password=PASS,
                                        database=DATABASE)

    # Construcción de la ventana principal & widgets
    window = Tk()
    window.iconbitmap('resources/logo.ico')
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
                rowsProducts.append([rowcomplet[2], rowcomplet[5], rowcomplet[3], rowcomplet[0]])

        TabProductos.insertDATA(rowsProducts, clear=True)

    def inStock():
        rowSelect = TabProductos.Treeview.item(TabProductos.Treeview.selection())
        cantStock = rowSelect['values'][1]
        idProduct = rowSelect['values'][2]

        textError = "No puedes añadir a la cesta de venta más cantidad de la que hay en inventario"


        items = CestaTable.Treeview.get_children()
        if items != ():
            countCesta = 0
            for i in items:
                if CestaTable.Treeview.item(i)['values'][2] == idProduct:
                    countCesta += CestaTable.Treeview.item(i)['values'][1]

            if countCesta < cantStock: return True
            else: messagebox.showerror('Erro de existencias', textError)


        else:
            if int(entry_cant.get()) <= cantStock: return TRUE
            else:
                messagebox.showerror('Eror', textError)
                return FALSE

    # Esta función será un ResponseHandler de TableFrame
    def submit_cest(event):
        try:

            focus_select = TabProductos.Treeview.item(TabProductos.Treeview.selection())

            nombreProducto = focus_select['text']
            precioProducto = float(focus_select['values'][0])
            cantidadProducto = int(entry_cant.get())
            productID = int(focus_select['values'][2])
            if inStock():
                if cantidadProducto > 0:
                    focus_select = [nombreProducto, precioProducto, cantidadProducto, productID]
                    CestaTable.insertDATA([tuple(focus_select)], clear=False)
                    TabProductos.Treeview.selection_remove(TabProductos.Treeview.selection())
                    entry_cant.delete(0, 'end')
                    SearchTabP.Entrada.delete(0, 'end')

                    montoAdicionalDeVenta = precioProducto * cantidadProducto
                    PanelDeVenta.elementosTransaccion(ventasP=montoAdicionalDeVenta)

                else:
                    messagebox.showerror('Oye, tranquilo viejo', 'Cantidad negativa? \nQué coño?')



        except:
            messagebox.showerror('Oye, tranquilo viejo', 'No se puede añadir eso.')

    SearchTabP = src.Search.Search(TableFrame)  # Entrada de busqueda
    TabProductos = src.Table.Tabla(TableFrame, height=17)  # Tabla de productos de busqueda
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
                    productoAEliminar = CestaTable.Treeview.item(item)
                    precioProducto = float(productoAEliminar['values'][0])
                    cantidadProducto = float(productoAEliminar['values'][1])

                    nuevoMontoDeVenta = -(precioProducto*cantidadProducto)
                    PanelDeVenta.elementosTransaccion(ventasP=nuevoMontoDeVenta, vueltoP= PanelDeVenta.vuelto_valor, pagoP= PanelDeVenta.pago_valor)
                    PanelDeVenta.calcularBton(event = None)

                    CestaTable.Treeview.delete(item)




            else:
                messagebox.showerror('Error', 'No has seleccionado nada')
        except:
            messagebox.showerror('Error', 'No se realizó la acción')

    # Frame de la cuenta
    PanelDeVenta = src.CuentaPago.CuentaPago(CestaFrame)

    # Frame de la cesta de compra
    CestaTable = src.Table.Tabla(CestaFrame, height=5)
    CestaTable.createTB(
        {'head': 'Producto', 'anchor': 'w', 'width': 150},
        {'head': 'Precio', 'anchor': 'center', 'width': 50},
        {'head': 'Cantidad', 'anchor': 'center', 'width': 75}
    )

    PanelDeVenta.set_DataObject(CestaTable)
    newConnect = src.Data.Ginerdata(host=HOST, user=USER, password=PASS,
                                        database=DATABASE)
    PanelDeVenta.set_connectSQL(newConnect)
    PanelDeVenta.set_canastaObject(CestaTable)
    PanelDeVenta.set_tableProducts(TabProductos)



    # Botón de borrar elemento de la cesta de compra
    DeleteCesta = Button(CestaFrame, text = "Eliminar de la cesta", relief = GROOVE)
    DeleteCesta.bind('<ButtonRelease-1>', del_icesta)
    DeleteCesta.grid(pady = 5)























    window.config(menu=src.Menu.SpecialMenu(window))
    window.mainloop()


if __name__ == '__main__':
    main()
