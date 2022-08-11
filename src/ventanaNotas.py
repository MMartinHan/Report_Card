from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk
from numpy import place
import ventana as v


class VentanaNotas(Frame):


    def __init__(self, master=None):
        super().__init__(master,width=800,height=350)
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
        frame2 = Frame(self,bg="#d3dde3" )
        frame2.place(x=0,y=0,width=200, height=350)   

        lbl1 = Label(frame2,text="ID.Nota ")
        lbl1.place(x=10,y=5)        
        self.txtIDnota=Entry(frame2)
        self.txtIDnota.place(x=25,y=25,width=100, height=20)  


        lbl2 = Label(frame2,text="ID.ESTUDIANTE ")
        lbl2.place(x=10,y=55)        
        self.txtIDestudiante=Entry(frame2)
        self.txtIDestudiante.place(x=25,y=75,width=100, height=20)  


        lbl3 = Label(frame2,text="NRC_MATERIA ")
        lbl3.place(x=10,y=105)        
        self.txtNRC=Entry(frame2)      
        self.txtNRC.place(x=25,y=125,width=100, height=20)


        lbl4 = Label(frame2,text="PARCIAL ")
        lbl4.place(x=10,y=155)        
        self.txtParcial=Entry(frame2)      
        self.txtParcial.place(x=25,y=180,width=100, height=20)


        lbl5 = Label(frame2,text="NOTA_VALOR ")
        lbl5.place(x=10,y=205)        
        self.txtNota_Valor=Entry(frame2)      
        self.txtNota_Valor.place(x=25,y=230,width=100, height=20)   


        lbl6 = Label(frame2,text="NOTA_DESCRIPCION ")
        lbl6.place(x=10,y=255)        
        self.txtNota_Descripcion=Entry(frame2)      
        self.txtNota_Descripcion.place(x=25,y=280,width=100, height=20)  


        self.btnGuardar=Button(frame2,text="Guardar", command=self.fGuardar, bg="green", fg="white")
        self.btnGuardar.place(x=15,y=315,width=60, height=30)
        self.btnCancelar=Button(frame2,text="Cancelar", command=self.fCancelar, bg="red", fg="white")
        self.btnCancelar.place(x=85,y=315,width=60, height=30)       
        self.grid = ttk.Treeview(self, columns=("col1","col2","col3","col4","col5"))        
        self.grid.column("#0",width=50)
        self.grid.column("col1",width=60, anchor=CENTER)
        self.grid.column("col2",width=90, anchor=CENTER)
        self.grid.column("col3",width=90, anchor=CENTER)
        self.grid.column("col4",width=90, anchor=CENTER)   
        self.grid.column("col5",width=90, anchor=CENTER)  
        self.grid.heading("#0", text="ID.N.", anchor=CENTER)
        self.grid.heading("col1", text="ID.E.", anchor=CENTER)
        self.grid.heading("col2", text="NRC.M.", anchor=CENTER)
        self.grid.heading("col3", text="PARCIAL", anchor=CENTER)
        self.grid.heading("col4", text="NOTA.VALOR", anchor=CENTER)
        self.grid.heading("col5", text="DESCRIPCION", anchor=CENTER)     
        self.grid.place(x=250,y=0,width=500, height=250)

    
        
  
    def fNuevo(self):         
        pass
    
    def fGuardar(self):
        Id_Nota = self.txtIDnota.get()
        Id_Estudiante = self.txtIDestudiante.get()
        NRC_Materia = self.txtNRC.get()
        Parcial = self.txtParcial.get()
        Nota_Valor = self.txtNota_Valor.get()
        Nota_Descripcion = self.txtNota_Descripcion.get()
        self.grid.insert("", 0, text=Id_Nota, values=(Id_Estudiante,NRC_Materia,Parcial,Nota_Valor,Nota_Descripcion))
        self.txtIDnota.delete(0,END)
        self.txtIDestudiante.delete(0,END)
        self.txtNRC.delete(0,END)
        self.txtParcial.delete(0,END)
        self.txtNota_Valor.delete(0,END)
        self.txtNota_Descripcion.delete(0,END)
        self.txtIDnota.focus()


    
    def fModificar(self):        
        pass
    
    def fEliminar(self):
        pass

    def fCancelar(self):
        Id_Nota = self.txtIDnota.get()
        Id_Estudiante = self.txtIDestudiante.get()
        NRC_Materia = self.txtNRC.get()
        Parcial = self.txtParcial.get()
        Nota_Valor = self.txtNota_Valor.get()
        Nota_Descripcion = self.txtNota_Descripcion.get()
        self.txtIDnota.delete(0,END)
        self.txtIDestudiante.delete(0,END)
        self.txtNRC.delete(0,END)
        self.txtParcial.delete(0,END)
        self.txtNota_Valor.delete(0,END)
        self.txtNota_Descripcion.delete(0,END)
        self.txtIDnota.focus()

   