from tkinter import *
from tkinter import ttk
import tkinter
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from numpy import place
import ventana as vnt
import conection as cnct


class VentanaNotas(Frame):


    def __init__(self, master=None):
        super().__init__(master,width=900,height=350)
        self.imagen()
        self.createwidgets()
        self.fMostrar()
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
        frame2.place(x=0,y=0,width=240, height=350)   

        lbl1 = Label(frame2,text="ID.Nota ")
        lbl1.place(x=10,y=5)        
        self.txtIDnota=Entry(frame2,justify="center")
        self.txtIDnota.place(x=25,y=25,width=140, height=20)  


        lbl2 = Label(frame2,text="ID.ESTUDIANTE ")
        lbl2.place(x=10,y=55)
        list_ste = cnct.recuperar_idEstudinte()       
        self.cmbEstudiante = ttk.Combobox(frame2,state="readonly",values=list_ste, justify=CENTER)
        list_ste=cnct.recuperar_idEstudiante()        
        self.cmbEstudiante = ttk.Combobox(frame2,width=10,state="readonly",values=list_ste, justify=CENTER)
        self.cmbEstudiante.place(x=25,y=75,width=140, height=20)  


        lbl3 = Label(frame2,text="NRC_MATERIA ")
        lista_nrc= cnct.obtener_nrc()
        lbl3.place(x=10,y=105)        
        self.cmbNrc=ttk.Combobox(frame2,width=10,state="readonly",values=lista_nrc, justify=CENTER)
        self.cmbNrc.place(x=25,y=125,width=140, height=20)      


        lbl4 = Label(frame2,text="PARCIAL ")
        lbl4.place(x=10,y=155)        
        self.cmbParcial=ttk.Combobox(frame2,width=10,state="readonly",values=["1","2","3"],justify=CENTER)
        self.cmbParcial.place(x=25,y=175,width=140, height=20)


        lbl5 = Label(frame2,text="NOTA_VALOR ")
        lbl5.place(x=10,y=205)        
        self.txtNota_Valor=Entry(frame2,justify=CENTER)      
        self.txtNota_Valor.place(x=25,y=230,width=140, height=20)   


        lbl6 = Label(frame2,text="NOTA_DESCRIPCION ")
        lbl6.place(x=10,y=255)        
        self.comboNota_Descripcion=ttk.Combobox(frame2,width=20,state="readonly",justify=CENTER,values=['FORO','PRUEBA_INTERMEDIA','TAREA','PRUEBA_CONJUNTA','LABORATORIO','TRABAJO_GRUPAL'])      
        self.comboNota_Descripcion.place(x=25,y=280,width=140, height=20)


        self.btnGuardar=Button(frame2,text="Guardar", command=self.fGuardar, bg="green", fg="white")
        self.btnGuardar.place(x=15,y=315,width=60, height=30)
        self.btnCancelar=Button(frame2,text="Cancelar", command=self.fCancelar, bg="red", fg="white")
        self.btnCancelar.place(x=85,y=315,width=60, height=30) 
        self.btnRegresar=Button(frame2,text="Regresar", command=self.fRegresar, bg="green", fg="white")
        self.btnRegresar.place(x=155,y=315,width=60, height=30)   
        
        self.btnNuevo=Button(text="Buscar",command=self.fBuscar, bg="blue", fg="white")
        self.btnNuevo.place(x=400,y=425,width=80, height=30 )        
        self.btnModificar=Button(text="Modificar",command=self.fModificar, bg="blue", fg="white")
        self.btnModificar.place(x=500,y=425,width=80, height=30)                
        self.btnEliminar=Button(text="Eliminar",command=self.fEliminar, bg="blue", fg="white")
        self.btnEliminar.place(x=600,y=425,width=80, height=30)   
        
        
        self.grid = ttk.Treeview(self, columns=("col1","col2","col3","col4","col5"))        
        self.grid.column("#0",width=50)
        self.grid.column("col1",width=90, anchor=CENTER)
        self.grid.column("col2",width=90, anchor=CENTER)
        self.grid.column("col3",width=90, anchor=CENTER)
        self.grid.column("col4",width=110, anchor=CENTER)   
        self.grid.column("col5",width=60, anchor=CENTER)  
        self.grid.heading("#0", text="ID NOTA", anchor=CENTER)
        self.grid.heading("col1", text="ID ESTUDIANTE", anchor=CENTER)
        self.grid.heading("col2", text="NRC MATERIA", anchor=CENTER)
        self.grid.heading("col3", text="NOTA VALOR", anchor=CENTER)
        self.grid.heading("col4", text="DESCRIPCION", anchor=CENTER)
        self.grid.heading("col5", text="PARCIAL", anchor=CENTER)     
        self.grid.place(x=250,y=0,width=600, height=250)
        

    def fNuevo(self):         
        pass
    
    def fMostrar(self):
        id_not,estudiante_id,materia_nrc,nota_valor,nota_descripcion,numero_parcial = cnct.actualizar_notas()
        for i in range(len(id_not)):
            self.grid.insert("",0,text=id_not[i],values=(estudiante_id[i],materia_nrc[i],nota_valor[i],nota_descripcion[i],numero_parcial[i]))
    
    def fGuardar(self):
        Id_Nota = self.txtIDnota.get()
        Id_Estudiante = self.cmbEstudiante.get()
        nrc = self.cmbNrc.get()
        Parcial = self.cmbParcial.get()
        Nota_Valor = self.txtNota_Valor.get()
        Nota_Descripcion = self.comboNota_Descripcion.get()

        #validacion de campos vacios
        if Id_Nota == "" or Id_Estudiante == "" or nrc == "" or Parcial == "" or Nota_Valor == "" or Nota_Descripcion == "" or Id_Nota.isdigit() == False :
            messagebox.showinfo("Error","Faltan campos por llenar o un campo no es valido")
        else:
            try:
                if cnct.buscar_id_nota(Id_Nota) == True:
                    messagebox.showinfo("Error","El ID de la nota ya existe")   
                else: 
                    if Nota_Valor.isdigit() == False or int(Nota_Valor) < 0 or int(Nota_Valor) > 20:
                        messagebox.showinfo("Error","El valor de la nota no es valido")
                    else:
                        cnct.insert_nota(Id_Nota,Id_Estudiante,nrc,Nota_Valor,Nota_Descripcion,Parcial)
                        #TABLA
                        self.grid.delete(*self.grid.get_children())
                        self.fMostrar()
                        self.txtIDnota.delete(0,END)
                        self.cmbEstudiante.set(' ')
                        self.cmbNrc.set(' ')
                        self.cmbParcial.set(' ')
                        self.txtNota_Valor.delete(0,END)
                        self.comboNota_Descripcion.set(' ')
                        self.txtIDnota.focus()
                    pass
            except Exception as e:
                messagebox.showinfo("Error", "El id ya existe")


    def fRegresar(self):
        self.master.destroy()
        root = Tk()
        root.wm_title("Registro de Notas")
        vnt.Ventana(root)
        root.mainloop()
    
    
    def fModificar(self):
        Id_Nota = self.txtIDnota.get()
        nrc = self.cmbNrc.get()
        Parcial = self.cmbParcial.get()
        Nota_Valor = self.txtNota_Valor.get()
        Nota_Descripcion = self.comboNota_Descripcion.get()

        if Nota_Valor.isdigit() == False or int(Nota_Valor) < 0.00 or int(Nota_Valor) > 20.00:
            messagebox.showinfo("Error","El valor de la nota no es valido")
        else:
            cnct.modificar_nota(Id_Nota,nrc,Nota_Valor,Nota_Descripcion,Parcial)
            self.grid.delete(*self.grid.get_children())
            self.fMostrar()
            self.txtIDnota.delete(0,END)
            self.cmbEstudiante.set(' ')
            self.cmbNrc.set(' ')
            self.cmbParcial.set(' ')
            self.txtNota_Valor.delete(0,END)
            self.comboNota_Descripcion.set(' ')
            self.txtIDnota.focus()

    def fBuscar(self):
        id_Estudiante : int
        nrc: int
        nota : int
        nota_descripcion : str
        parcial : int
        Id_Nota = self.txtIDnota.get()

        if Id_Nota == "":
            messagebox.showinfo("Error","El campo ID esta vacio")
            self.txtID.focus()
        else:
            if cnct.buscar_id_nota(Id_Nota):
                id_Estudiante = cnct.buscar_idEstudiante(Id_Nota)
                self.cmbEstudiante.set(id_Estudiante)
                nrc = cnct.buscar_nrc(Id_Nota)
                self.cmbNrc.set(nrc)
                
                nota = cnct.buscar_notaValor(Id_Nota)
                self.txtNota_Valor.insert(0,nota)

                nota_descripcion = cnct.buscar_notaDescripcion(Id_Nota)
                self.comboNota_Descripcion.set(nota_descripcion)
                parcial = cnct.buscar_parcial(Id_Nota)
                self.cmbParcial.set(parcial)
            else:
                messagebox.showinfo("Error","El ID no existe")
                self.txtIDnota.delete(0,END)
                self.txtIDnota.focus()
        
    def fEliminar(self):
        Id_Nota = self.txtIDnota.get()
        cnct.eliminar_nota(Id_Nota)
        self.grid.delete(*self.grid.get_children())
        self.fMostrar()
        self.txtIDnota.delete(0,END)
        self.cmbEstudiante.set(' ')
        self.cmbNrc.set(' ')
        self.txtNota_Valor.delete(0,END)
        self.cmbParcial.set(' ')
        self.comboNota_Descripcion.set(' ')
        self.txtIDnota.focus()
        

    def fCancelar(self):
        Id_Nota = self.txtIDnota.get()
        Id_Estudiante = self.cmbEstudiante.get()
        Nota_Valor = self.txtNota_Valor.get()
        self.txtIDnota.delete(0,END)
        self.cmbEstudiante.set(' ')
        self.cmbNrc.set(' ')
        self.txtNota_Valor.delete(0,END)
        self.cmbParcial.set(' ')
        self.comboNota_Descripcion.set(' ')
        Nota_Descripcion = self.comboNota_Descripcion.get()
        self.txtIDnota.set('')
        self.cmbEstudiante.set('')
        self.cmbNrc.set('')
        self.cmbParcial.set('')
        self.txtNota_Valor.set('')
        self.comboNota_Descripcion.set('')
        self.txtIDnota.focus()

    
   