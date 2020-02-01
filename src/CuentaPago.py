from tkinter import *


class CuentaPago(Frame):

    def __init__(self, master=None, coorgrid=(0, 0)):
        super().__init__(master, relief=SOLID, highlightbackground="#D3D3D3", highlightcolor="#D3D3D3", highlightthickness=1,)
        self.grid(row = coorgrid[0], column = coorgrid[1], pady = 20)

        # Frames dentro del Frame CuentaPago
        self.Internel = Frame(self)
        self.Internel.grid(row = 0, column = 0, pady = 35, padx = 35)

        self.Internel2 = Frame(self)
        self.Internel2.grid(row = 1, column = 0)

        # Variables necesarias de la clase
        self.venta_valor = 0
        self.vuelto_valor = 0

        # Contrucción inicial del marco
        self.elementosTransaccion()


    def calcularBton(self, event, vuelto):
        self.elementosTransaccion(self.venta_valor, vuelto)


    def elementosTransaccion(self, ventasP = 0, vueltoP = 0, pagoP = 0):
        '''

        Este método no hace cáculos. Sólo construye el Frame que muestra los velores de venta.

        :param ventasP: Valor del monto vendido
        :param vueltoP: Valor del monto a devolver
        :return: Retorna una tupla de la forma (ventasP,vueltoP)
        '''


        # Label de ventas
        label_ventas = Label(self.Internel, text = "Ventas:")
        label_ventas.grid(row = 0, column = 0, sticky = "w")

        # Valor de ventas
        label_ventas_valor = Label(self.Internel, text = ventasP)
        label_ventas_valor.grid(row = 0, column = 1)

        # Label de pago
        label_pago = Label(self.Internel, text = "Pago:")
        label_pago.grid(row = 1, column = 0, sticky = "w")

        # Entrada del monto con el que paga el vendedor
        entry_pago = Entry(self.Internel, width = 20, justify='center')
        entry_pago.insert(0, pagoP)
        entry_pago.grid(row = 1, column = 1, padx = 3)

        # Botón de calcular vuelto
        calcular_bton = Button(self.Internel, text = "Calcular vuelto", relief = GROOVE)
        calcular_bton.bind('<ButtonRelease-1>', lambda a: self.calcularBton(a, self.vuelto_valor))
        calcular_bton.grid(row = 2, column = 1, padx = 5, pady = 5)

        # Label de vuelto
        label_vuelto = Label(self.Internel, text = "Vuelto:")
        label_vuelto.grid(row = 3, column = 0, sticky = "w")

        # Valor de vuelto
        label_vuelto_valor = Label(self.Internel, text = vueltoP)
        label_vuelto_valor.grid(row = 3, column = 1)

        return label_ventas_valor.cget("text"), label_vuelto_valor.cget('text')










if __name__ == '__main__':
    window = Tk()
    a = CuentaPago(window, coorgrid=(0,0))


    window.mainloop()
