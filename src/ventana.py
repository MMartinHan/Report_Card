from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk
from numpy import place
from ventanaEstudiante import *
from ventanaNotas import *
from ventanaPromedio import *

class Ventana(Frame):


    def __init__(self, master=None):
        super().__init__(master,width=500,height=200)
        self.imagen()
        self.Botones()
        self.master = master
        self.pack()
        

    def imagen(self):
        img1 = Image.open("espe.png")
        img1 = img1.resize((520,150))
        img2 = ImageTk.PhotoImage(img1)
        label1 = Label(image=img2)
        label1.image = img2
        label1.pack()

    def Botones(self):
        boton1 = Button(self, text="Agregar Estudiante ", command=self.fAgregarEstudiante)
        boton1.place(x=180, y=10, width=150, height=30)
        boton2 = Button(self, text="Agregar Notas", command=self.fAgregarNotas)
        boton2.place(x=180, y=50,width=150, height=30)
        boton3 = Button(self, text="Mostrar Notas Finales", command=self.fPromedio)
        boton3.place(x=180, y=90,width=150, height=30)
        
        

    def fAgregarEstudiante(self):
        self.master.destroy()
        root = Tk()
        root.wm_title("Registro de Estudiantes")
        VentanaEstudiante(root)
        root.mainloop()

    def fAgregarNotas(self):
        self.master.destroy()
        root = Tk()
        root.wm_title("Registro de Notas")
        VentanaNotas(root)
        root.mainloop()
    
    def fPromedio(self):
        self.master.destroy()
        root = Tk()
        root.wm_title("Promedio Final")
        VentanaPromedio(root)
        root.mainloop()
        

    def fNuevo(self):         
        pass
    
    def fGuardar(self):        
        pass
    
    def fModificar(self):        
        pass
    
    def fEliminar(self):
        pass

    def fCancelar(self):
        pass
