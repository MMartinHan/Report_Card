from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk
from numpy import place
import ventana as vnt

class VentanaPromedio(Frame):


    def __init__(self, master=None):
        super().__init__(master,width=700,height=300)
        self.imagen()
        self.createwidgets()
        self.master = master
        self.pack()
        

    def imagen(self):
        img1 = Image.open("img/espe.png")
        img1 = img1.resize((520,150))
        img2 = ImageTk.PhotoImage(img1)
        label1 = Label(image=img2)
        label1.image = img2
        label1.pack()

    def createwidgets(self):
        lbl1 = Label(text="Ingrese el ID del Estudiante: ")
        lbl1.place(x=100,y=150)
        self.txtIDestudiante=Entry(width=100)
        self.txtIDestudiante.place(x=100,y=175,width=100, height=20)
        self.btnBuscar = Button(text="Buscar",command=self.fBuscar)
        self.btnBuscar.place(x=100,y=200,width=50, height=20)
        self.btnRegresar=Button(text="Regresar", command=self.fRegresar)
        self.btnRegresar.place(x=605,y=410,width=80, height=30)
        self.grid = ttk.Treeview(self, columns=("col1","col2","col3"))        
        self.grid.column("#0",width=50)
        self.grid.column("col1",width=60, anchor=CENTER)
        self.grid.column("col2",width=90, anchor=CENTER)
        self.grid.column("col3",width=90, anchor=CENTER)   
        self.grid.heading("#0", text="Id", anchor=CENTER)
        self.grid.heading("col1", text="Nombre", anchor=CENTER)
        self.grid.heading("col2", text="NRC", anchor=CENTER)
        self.grid.heading("col3", text="Nota Final", anchor=CENTER)
        self.grid.place(x=125,y=80,width=420, height=150)

        
    def fBuscar(self):
        pass

    def fRegresar(self):
        self.master.destroy()
        root = Tk()
        root.wm_title("Registro de Estudiantes")
        vnt.Ventana(root)
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

   