from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk
from numpy import place
import ventana as vnt
import conection as cnct

class VentanaPromedio(Frame):


    def __init__(self, master=None):
        super().__init__(master,width=700,height=300)
        self.imagen()
        self.createwidgets()
        self.master = master
        self.pack()
        

    def imagen(self):
        img1 = Image.open("espe.png")
        img1 = img1.resize((520,150))
        img2 = ImageTk.PhotoImage(img1)
        label1 = Label(image=img2)
        label1.image = img2
        label1.pack()

    def createwidgets(self):
        lbl1 = Label(text=" BUQUEDA DE DATOS ", font=("Arial Bold", 12))
        lbl1.place(x=260,y=150)
        lbl2 = Label(text="ID Estudiante", font=("Arial Bold", 12))
        lbl2.place(x=150,y=200)
        lbl3 = Label(text="NRC", font=("Arial Bold", 12))
        lbl3.place(x=290,y=200)
        lbl3 = Label(text="Parcial", font=("Arial Bold", 12))
        lbl3.place(x=370,y=200)

        lista_Estudiantes = cnct.recuperar_idEstudiante()
        self.cmbIDEstudiante =ttk.Combobox(width=80,state="readonly",values=lista_Estudiantes, justify=CENTER)
        self.cmbIDEstudiante.place(x=160,y=230,width=80, height=20)


        lista_nrc=cnct.obtener_nrc()
        self.cmbNrc=ttk.Combobox(width=60,state="readonly",values=lista_nrc, justify=CENTER)
        self.cmbNrc.place(x=280,y=230,width=60, height=20)

        self.cmbParcial=ttk.Combobox(width=80,state="readonly",values=["1","2","3"], justify=CENTER)
        self.cmbParcial.place(x=370,y=230,width=80, height=20)    


        self.btnBuscar = Button(text="Buscar",command=self.mostrardatos_Parcial, width=80 , height=50 , bg="Blue", fg="white")
        self.btnBuscar.place(x=500,y=200,width=80, height=50)
        self.btnRegresar=Button(text="Regresar", command=self.fRegresar)
        self.btnRegresar.place(x=605,y=410,width=80, height=30)

        
    def fBuscar(self):
        pass

    def fRegresar(self):
        self.master.destroy()
        root = Tk()
        root.wm_title("Registro de Estudiantes")
        vnt.Ventana(root)
        root.mainloop()

    def mostrardatos_IdEstudiante(self):
        self.grid = ttk.Treeview(self, columns=("col1","col2"))        
        self.grid.column("#0",width=50)
        self.grid.column("col1",width=60, anchor=CENTER)
        self.grid.column("col2",width=90, anchor=CENTER)
        self.grid.heading("#0", text="ID ESTUDIANTE", anchor=CENTER)
        self.grid.heading("col1", text="NRC", anchor=CENTER)
        self.grid.heading("col2", text="NOTA FINAL", anchor=CENTER)
        self.grid.place(x=125,y=120,width=420, height=150)

        id_estudiante,nrc,nota_final=cnct.buscar_notas_IDEsudiante(self.cmbIDEstudiante.get())
        for i in range(len(id_estudiante)):
            self.grid.insert("",i,text=id_estudiante[i], values=(nrc[i],nota_final[i]))
        pass

    def mostrardatos_Nrc(self):
        pass


    def mostrardatos_Parcial(self):
        self.grid = ttk.Treeview(self, columns=("col1","col2","col3"))        
        self.grid.column("#0",width=50)
        self.grid.column("col1",width=60, anchor=CENTER)
        self.grid.column("col2",width=90, anchor=CENTER)
        self.grid.column("col3",width=90, anchor=CENTER)   
        self.grid.heading("#0", text="ID ESTUDIANTE", anchor=CENTER)
        self.grid.heading("col1", text="NRC", anchor=CENTER)
        self.grid.heading("col2", text="DESCRIPCION", anchor=CENTER)
        self.grid.heading("col3", text="NOTA VALOR", anchor=CENTER)
        self.grid.place(x=125,y=120,width=420, height=150)

        id_estudiante , nrc, nota_valor, descripcion = cnct.buscar_notas_Parcial(self.cmbParcial.get())
        for i in range(len(id_estudiante)):
            self.grid.insert("",0,text=id_estudiante[i], values=(nrc[i],nota_valor[i],descripcion[i]))
        

   