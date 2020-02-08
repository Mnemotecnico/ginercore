import tkinter
import src.Data
import keys
import src.Inventory.Editor
import src.Inventory.Agregador

def main(conector):
    window = tkinter.Tk()
    window.iconbitmap('resources/logo.ico')
    window.title('Editor del inventario')

    agregador = src.Inventory.Agregador.Inventory(window)
    editor = src.Inventory.Editor.Editor(window)

    agregador.set_conectorSQL(conector)
    editor.set_sqlObject(conector)

    agregador.grid(row = 0)
    editor.Frame.grid(row = 1)

    window.mainloop()

if __name__ == '__main__':
    conector = src.Data.Ginerdata(keys.USER, keys.HOST, keys.PASS, keys.DATABASE)
    main(conector)