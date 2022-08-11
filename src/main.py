from tkinter import *
from venv import create
from ventana import *


def main():
    root = Tk()
    root.wm_title("Registro de Notas")
    Ventana(root)
    root.mainloop()



if __name__ == "__main__":
    main()
    
