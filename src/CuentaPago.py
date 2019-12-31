from tkinter import *


class CuentaPago(Frame):
    def __init__(self, master=None, coorgrid=(0, 0)):
        super().__init__(master, relief=SOLID, highlightbackground="#D3D3D3", highlightcolor="#D3D3D3", highlightthickness=1,)
        self.grid(row = coorgrid[0], column = coorgrid[1])

        #Frames dentro del Frame CuentaPago
        self.Internel = Frame(self)
        self.Internel.grid()

        # Variables necesarias de la clase
        self.venta_valor = 0
        self.vuelto_valor = 0

        # Contrucción inicial del marco
        self.elementosTransaccion()


    def elementosTransaccion(self, ventasP = 0):
        label_ventas = Label(self.Internel, text = "Ventas:")
        label_ventas.grid(row = 0, column = 0, sticky = "w")

        label_ventas_valor = Label(self.Internel, text = self.venta_valor)
        label_ventas_valor.grid(row = 0, column = 1)

        label_pago = Label(self.Internel, text = "Pago:")
        label_pago.grid(row = 1, column = 0, sticky = "w")

        entry_pago = Entry(self.Internel)
        entry_pago.grid(row = 1, column = 1)








if __name__ == '__main__':
    window = Tk()
    a = CuentaPago(window, coorgrid=(0,0))

    window.mainloop()
