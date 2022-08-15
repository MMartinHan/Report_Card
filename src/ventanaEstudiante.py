from logging import root
from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk
from numpy import place
import ventana as vnt
import conection as cnct


class VentanaEstudiante(Frame):


    def __init__(self, master=None):
        super().__init__(master,width=600,height=260)
        self.imagen()
        self.createwidgets()
        self.fMostrarDatos()
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
        frame1 = Frame(self, bg="#bfdaff")
        frame1.place(x=0,y=0,width=93, height=259)        
        self.btnNuevo=Button(frame1,text="Buscar", command=self.fBuscar, bg="blue", fg="white")
        self.btnNuevo.place(x=5,y=50,width=80, height=30 )        
        self.btnModificar=Button(frame1,text="Modificar", command=self.fModificar, bg="blue", fg="white")
        self.btnModificar.place(x=5,y=90,width=80, height=30)                
        self.btnEliminar=Button(frame1,text="Eliminar", command=self.fEliminar, bg="blue", fg="white")
        self.btnEliminar.place(x=5,y=130,width=80, height=30)  
        self.btnRegresar=Button(frame1,text="Regresar", command=self.fRegresar)
        self.btnRegresar.place(x=5,y=170,width=80, height=30)              
        frame2 = Frame(self,bg="#d3dde3" )
        frame2.place(x=95,y=0,width=150, height=259)                        
        lbl1 = Label(frame2,text="ID.Estudiante: ")
        lbl1.place(x=2,y=5)        
        self.txtID=Entry(frame2)
        self.txtID.place(x=3,y=25,width=100, height=20)                
        lbl2 = Label(frame2,text="Nombre : ")
        lbl2.place(x=3,y=55)        
        self.txtName=Entry(frame2)
        self.txtName.place(x=3,y=75,width=100, height=20)        
        lbl3 = Label(frame2,text="Apellido : ")
        lbl3.place(x=3,y=105)        
        self.txtlastName=Entry(frame2)      
        self.txtlastName.place(x=3,y=125,width=100, height=20)        
        self.btnGuardar=Button(frame2,text="Guardar", command=self.fGuardar,bg="green", fg="white")
        self.btnGuardar.place(x=10,y=180,width=60, height=30)
        self.btnCancelar=Button(frame2,text="Cancelar", command=self.fCancelar, bg="red", fg="white")
        self.btnCancelar.place(x=80,y=180,width=60, height=30)        
        self.grid = ttk.Treeview(self, columns=("col1","col2"))        
        self.grid.column("#0",width=50)
        self.grid.column("col1",width=60, anchor=CENTER)
        self.grid.column("col2",width=90, anchor=CENTER)     
        self.grid.heading("#0", text="ID", anchor=CENTER)
        self.grid.heading("col1", text="Nombre", anchor=CENTER)
        self.grid.heading("col2", text="Apellido", anchor=CENTER)    
        self.grid.place(x=250,y=0,width=330, height=250)



    def fRegresar(self):
        self.master.destroy()
        root = Tk()
        root.wm_title("Registro de Notas")
        vnt.Ventana(root)
        root.mainloop()

    def fNuevo(self):
        pass

    def fMostrarDatos(self):
        id,nombre,apellido = cnct.actualizar()
        for i in range(len(id)):
            self.grid.insert("", 0, text=id[i], values=(nombre[i], apellido[i]))    
        
    def fBuscar(self):

        id = self.txtID.get()
        name : str
        name = cnct.buscar_nombre(id)
        self.txtName.insert(0, name)
        lastName = cnct.buscar_apellido(id)
        self.txtlastName.insert(0, lastName)       
        
    def fGuardar(self):
        id = self.txtID.get()
        name = self.txtName.get()
        name = name.upper()
        lastName = self.txtlastName.get()
        lastName = lastName.upper()
        cnct.insert_student(id,name,lastName)
        self.grid.delete(*self.grid.get_children())
        self.fMostrarDatos()
        
        #tabla
        
        

    
    def fModificar(self):  
        id = self.txtID.get()
        name = self.txtName.get()
        name = name.upper()
        lastName = self.txtlastName.get()
        lastName = lastName.upper()
        cnct.modificar_estudiante(id,name,lastName)
        self.grid.insert("", 0, text=id, values=(name, lastName))
        self.txtID.delete(0, END)
        self.txtName.delete(0, END)
        self.txtlastName.delete(0, END)
        self.txtID.focus()      
        
    
    def fEliminar(self):
        id = self.txtID.get()
        cnct.eliminar_estudiante(id)
        pass

    def fCancelar(self):
        id = self.txtID.get()
        name = self.txtName.get()
        lastName = self.txtlastName.get()
        self.txtID.delete(0, END)
        self.txtName.delete(0, END)
        self.txtlastName.delete(0, END)
        self.txtID.focus()
        
 

   