from tkinter import *
import time
from tkinter import messagebox
import src.Data

class CuentaPago(Frame):

    def __init__(self, master=None, coorgrid=(0, 0)):
        super().__init__(master, relief=SOLID, highlightbackground="#D3D3D3", highlightcolor="#D3D3D3", highlightthickness=1,)
        self.grid(row = coorgrid[0], column = coorgrid[1], pady = 20)

        # Frames dentro del Frame CuentaPago
        self.Internel = Frame(self)
        self.Internel.grid(row = 0, column = 0, pady = 35, padx = 35)

        self.Internel2 = Frame(self)
        self.Internel2.grid(row = 1, column = 0)

        self.Internel3 = Frame(self)
        self.Internel3.grid(row = 2, column = 0)

        # Variables necesarias de la clase
        self.venta_valor = 0.0
        self.vuelto_valor = 0.0
        self.dataObject = None
        self.conectorSQL = None
        self.cestaObject = None
        self.tableProducts = None

        # Contrucción inicial del marco
        self.elementosTransaccion()
        self.realizarVenta()

    def set_tableProducts(self, tableProducts):
        self.tableProducts = tableProducts

    def set_canastaObject(self, canastaObject):
        self.cestaObject = canastaObject

    def set_connectSQL(self, conectorSQL):
        self.conectorSQL = conectorSQL


    def set_DataObject(self, dataObject):
        self.dataObject = dataObject

    # Limpiar el objeto de tableProducts
    def clearTabProducts(self):
        if self.tableProducts != None:
            items = self.tableProducts.Treeview.get_children()
            self.tableProducts.Treeview.delete(*items)



    def calcularBton(self, event):
        montoDeVenta = float(self.venta_valor)
        cantidadDePago = float(self.entry_pago.get())
        vuelto = cantidadDePago - montoDeVenta
        self.elementosTransaccion(vueltoP = vuelto, pagoP= cantidadDePago)

    def realizarVenta(self):
        ventaBoton = Button(self.Internel3, text = "Registrar venta", relief = GROOVE, width = 35)
        ventaBoton.bind('<ButtonRelease-1>', self.dataSellToSQL)
        ventaBoton.grid()


    def dataSellToSQL(self, event):
        date = time.strftime('%Y-%m-%d %H:%M:%S')
        MessageConfirm = "Esta acción modificará la base de datos."
        proccessAllowed = messagebox.askquestion("Registrar venta", MessageConfirm)

        if TRUE:
            items = self.dataObject.Treeview.get_children()
            contenedorDeItems = []
            for item in items:
                valuesProduct = self.dataObject.Treeview.item(item)

                valuesProduct = [valuesProduct['values'][2],
                                 valuesProduct['values'][1]
                                 ]
                contenedorDeItems.append(valuesProduct)

            # Este método es de la clase Data
            self.conectorSQL.registrarTransaccion(contenedorDeItems, date)

            # Vaciar el canasto de venta
            itemsDeLaCanasta = self.cestaObject.Treeview.get_children()
            for i in itemsDeLaCanasta: self.cestaObject.Treeview.delete(i)

            # Vaciar el panel de venta
            self.elementosTransaccion(init=TRUE)

            # Vaciar la tabla de productos
            self.clearTabProducts()





    def elementosTransaccion(self, ventasP = 0.0, vueltoP = 0.0, pagoP = 0.0, init = FALSE):
        '''

        Este método no hace cáculos. Sólo construye el Frame que muestra los velores de venta.

        :param ventasP: Valor del monto vendido
        :param vueltoP: Valor del monto a devolver
        :return: Retorna una tupla de la forma (ventasP,vueltoP)
        '''
        if init == FALSE:
            self.venta_valor += ventasP
            self.pago_valor = pagoP
            self.vuelto_valor = vueltoP
        else :
            self.venta_valor = 0.0
            self.pago_valor = 0
            self.vuelto_valor = 0.0

        # Label de ventas
        label_ventas = Label(self.Internel, text = "Venta:")
        label_ventas.grid(row = 0, column = 0, sticky = "w")

        # Valor de ventas
        label_ventas_valor = Label(self.Internel, text = '$'+str(self.venta_valor))
        label_ventas_valor.grid(row = 0, column = 1)

        # Label de pago
        label_pago = Label(self.Internel, text = "Pago:")
        label_pago.grid(row = 1, column = 0, sticky = "w")

        # Entrada del monto con el que paga el vendedor
        self.entry_pago = Entry(self.Internel, width = 20, justify='center')
        self.entry_pago.insert(0, self.pago_valor)
        self.entry_pago.grid(row = 1, column = 1, padx = 3)
        self.entry_pago.bind("<Button-1>", self.clearEntry)

        # Botón de calcular vuelto
        calcular_bton = Button(self.Internel, text = "Calcular vuelto", relief = GROOVE)
        calcular_bton.bind('<ButtonRelease-1>', self.calcularBton)
        calcular_bton.grid(row = 2, column = 1, padx = 5, pady = 5)

        # Label de vuelto
        label_vuelto = Label(self.Internel, text = "Vuelto:")
        label_vuelto.grid(row = 3, column = 0, sticky = "w")

        # Valor de vuelto
        label_vuelto_valor = Label(self.Internel, text = '$'+str(self.vuelto_valor))
        label_vuelto_valor.grid(row = 3, column = 1)

        return label_ventas_valor.cget("text"), label_vuelto_valor.cget('text')


    def clearEntry(self, event):
        self.entry_pago.delete(0, "end")










if __name__ == '__main__':
    window = Tk()
    a = CuentaPago(window, coorgrid=(0,0))


    window.mainloop()
