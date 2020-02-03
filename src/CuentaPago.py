from tkinter import *
import datetime
from tkinter import messagebox

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
        self.venta_valor = 0
        self.vuelto_valor = 0
        self.dataObject = None

        # Contrucción inicial del marco
        self.elementosTransaccion()
        self.realizarVenta()

    def set_DataObject(self, dataObject):
        self.dataObject = dataObject

    def currentDate(self):
        date = datetime.datetime.now()
        year = date.year
        month = date.month
        day = date.day
        hour = date.hour
        minute = date.minute
        second = date.second

        return str(year)+'-'+str(month)+'-'+str(day)+' '+str(hour)+':'+str(minute)+':'+str(second)


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
        date = self.currentDate()
        MessageConfirm = "Esta acción modificará la base de datos."
        proccessAllowed = messagebox.askquestion("Registrar venta", MessageConfirm)

        if TRUE:
            items = self.dataObject.Treeview.get_children()
            print(items)
            # continuar desde aquí




    def elementosTransaccion(self, ventasP = 0, vueltoP = 0, pagoP = 0):
        '''

        Este método no hace cáculos. Sólo construye el Frame que muestra los velores de venta.

        :param ventasP: Valor del monto vendido
        :param vueltoP: Valor del monto a devolver
        :return: Retorna una tupla de la forma (ventasP,vueltoP)
        '''
        self.venta_valor += ventasP
        self.pago_valor = pagoP
        self.vuelto_valor = vueltoP

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
