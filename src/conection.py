from decouple import config
from supabase import create_client, Client
import re

url: str = config("SUPABASE_URL")
key: str = config("SUPABASE_KEY")
supabase: Client = create_client(url, key)

def insert_student(id: int, first_name: str, last_name: str):
    url: str = config("SUPABASE_URL")
    key: str = config("SUPABASE_KEY")
    supabase: Client = create_client(url, key)
    data = supabase.table("estudiante").insert({"id": id, "first_name": first_name, "last_name": last_name}).execute()
    
def obtener_nrc():
    url: str = config("SUPABASE_URL")
    key: str = config("SUPABASE_KEY")
    supabase: Client = create_client(url, key)
    data = supabase.table("materia").select("nrc").execute()
    data = supabase.table("materia").select("nrc").execute().json()
    data = re.findall('[0-9]+',data)
    return data

def guardar_datos_txt(id: int, first_name: str, last_name: str):
    archivo = open("estudiante.txt","w")
    archivo.write(str(id)+","+first_name+","+last_name+"\n")
    archivo.close()


def modificar_estudiante(id: int , first_name: str, last_name: str):
    url: str = config("SUPABASE_URL")
    key: str = config("SUPABASE_KEY")
    supabase: Client = create_client(url, key)
    supabase.table('estudiante').update({"id": id, "first_name": first_name, "last_name": last_name}).eq("id",id).execute()
    

def insert_nota(id: int, estudiante: str, nrc: int, nota: float, descripcion: str, parcial: int):
    url: str = config("SUPABASE_URL")
    key: str = config("SUPABASE_KEY")
    supabase: Client = create_client(url, key)
    data = supabase.table("notas").insert({"id_not": id, "estudiante_id": estudiante, "materia_nrc": nrc, "nota_valor": nota, "nota_descripcion": descripcion, "numero_parcial": parcial}).execute()

    
def buscar_nombre(id: int):
    first_name: str
    url: str = config("SUPABASE_URL")
    key: str = config("SUPABASE_KEY")
    supabase: Client = create_client(url, key)
    supabase.table("estudiante").select("*").eq("id",id).execute()
    for item  in supabase.table("estudiante").select("*").eq("id",id).execute().data:
        first_name = item["first_name"]
    return first_name

def buscar_apellido(id: int):
    last_Name: str
    url: str = config("SUPABASE_URL")
    key: str = config("SUPABASE_KEY")
    supabase: Client = create_client(url, key)
    supabase.table("estudiante").select("*").eq("id",id).execute()
    for item  in supabase.table("estudiante").select("*").eq("id",id).execute().data:
        last_Name = item["last_name"]
    return last_Name

def eliminar_estudiante(id: int):
    url: str = config("SUPABASE_URL")
    key: str = config("SUPABASE_KEY")
    supabase: Client = create_client(url, key)
    supabase.table('estudiante').delete().eq("id",id).execute()


def modificar_nota(idNota : int ,nrc: int, nota: float, descripcion: str, parcial: int):
    url: str = config("SUPABASE_URL")
    key: str = config("SUPABASE_KEY")
    supabase: Client = create_client(url, key)
    supabase.table('notas').update({"id_not": idNota,"materia_nrc": nrc, "nota_valor": nota, "nota_descripcion": descripcion, "numero_parcial": parcial}).eq("id_not",idNota).execute() 
    

def actualizar ():
    url: str = config("SUPABASE_URL")
    key: str = config("SUPABASE_KEY")
    supabase: Client = create_client(url, key)
    id = []
    nombre = []
    apellido = []
    for item  in supabase.table("estudiante").select("*").execute().data:
        id.append(item["id"])
        nombre.append(item["first_name"])
        apellido.append(item["last_name"])
    return id, nombre, apellido

def recuperar_idEstudiante():
    url: str = config("SUPABASE_URL")
    key: str = config("SUPABASE_KEY")
    supabase: Client = create_client(url, key)
    id_est = []
    for item  in supabase.table("estudiante").select("*").execute().data:
        id_est.append(item["id"])
    return id_est

def actualizar_notas():
    url: str = config("SUPABASE_URL")
    key: str = config("SUPABASE_KEY")
    supabase: Client = create_client(url, key)
    id_not = []
    estuadiante_id = []
    materia_nrc = []
    nota_valor = []
    nota_descripcion = []
    numero_parcial = []
    for item  in supabase.table("notas").select("*").execute().data:
        id_not.append(item["id_not"])
        estuadiante_id.append(item["estudiante_id"])
        materia_nrc.append(item["materia_nrc"])
        nota_valor.append(item["nota_valor"])
        nota_descripcion.append(item["nota_descripcion"])
        numero_parcial.append(item["numero_parcial"])
    return id_not,estuadiante_id,materia_nrc,nota_valor,nota_descripcion,numero_parcial

def obtener_notas_parcial(id_est: str,nrc: int, parcial: int):
    url: str = config("SUPABASE_URL")
    key: str = config("SUPABASE_KEY")
    supabase: Client = create_client(url, key)
    nota = []
    for item  in supabase.table("notas").select("*").eq("estudiante_id",id_est).eq("materia_nrc",nrc).eq("numero_parcial",parcial).execute().data:
        nota.append(item["nota_valor"])
    return nota

def obtener_promedio_final(id_est: str, nrc: int):
    lista_promedio = []
    parcial1 = obtener_notas_parcial(id_est,nrc,1)
    promedio1 = calculo_promedio_parcial(parcial1)
    parcial2 = obtener_notas_parcial(id_est,nrc,2)
    promedio2 = calculo_promedio_parcial(parcial2)
    parcial3 = obtener_notas_parcial(id_est,nrc,3)
    promedio3 = calculo_promedio_parcial(parcial3)
    lista_promedio.append(promedio1)
    lista_promedio.append(promedio2)
    lista_promedio.append(promedio3)
    promedio_final = calculo_promedio_final(lista_promedio)
    return promedio_final


def calculo_promedio_parcial(list_notas: list):
    suma = 0
    for item in list_notas:
        suma += item
    promedio = suma/6
    return promedio

def calculo_promedio_final(list_notas: list):
    suma = 0
    for item in list_notas:
        suma += item
    promedio = suma/3
    return promedio

def obtener_nombre():
    url: str = config("SUPABASE_URL")
    key: str = config("SUPABASE_KEY")
    supabase: Client = create_client(url, key)
    

def buscar_idEstudiante(id: int):
    url: str = config("SUPABASE_URL")
    key: str = config("SUPABASE_KEY")
    supabase: Client = create_client(url, key)
    supabase.table("notas").select("*").eq("id_not",id).execute()
    for item  in supabase.table("notas").select("*").eq("id_not",id).execute().data:
        return item["estudiante_id"]

def buscar_nrc(id: int):
    url: str = config("SUPABASE_URL")
    key: str = config("SUPABASE_KEY")
    supabase: Client = create_client(url, key)
    supabase.table("notas").select("*").eq("id_not",id).execute()
    for item  in supabase.table("notas").select("*").eq("id_not",id).execute().data:
        return item["materia_nrc"]

def buscar_notaValor(id: int):
    url: str = config("SUPABASE_URL")
    key: str = config("SUPABASE_KEY")
    supabase: Client = create_client(url, key)
    supabase.table("notas").select("*").eq("id_not",id).execute()
    for item  in supabase.table("notas").select("*").eq("id_not",id).execute().data:
        return item["nota_valor"]

def buscar_notaDescripcion(id: int):
    url: str = config("SUPABASE_URL")
    key: str = config("SUPABASE_KEY")
    supabase: Client = create_client(url, key)
    supabase.table("notas").select("*").eq("id_not",id).execute()
    for item  in supabase.table("notas").select("*").eq("id_not",id).execute().data:
        return item["nota_descripcion"]

def buscar_parcial(id: int):
    url: str = config("SUPABASE_URL")
    key: str = config("SUPABASE_KEY")
    supabase: Client = create_client(url, key)
    supabase.table("notas").select("*").eq("id_not",id).execute()
    for item  in supabase.table("notas").select("*").eq("id_not",id).execute().data:
        return item["numero_parcial"]


def recuperar_idEstudinte():
    url: str = config("SUPABASE_URL")
    key: str = config("SUPABASE_KEY")
    supabase: Client = create_client(url, key)
    id_est =[]
    for item  in supabase.table("estudiante").select("*").execute().data:
        id_est.append(item["id"])
    return id_est
    
def eliminar_nota(id: int):
    url: str = config("SUPABASE_URL")
    key: str = config("SUPABASE_KEY")
    supabase: Client = create_client(url, key)
    supabase.table('notas').delete().eq("id_not",id).execute()


def buscar_notas_Parcial(parcial : int):
    estudiante_id = []
    nrc_materia = []
    descripcion = []
    valor = []
    url: str = config("SUPABASE_URL")
    key: str = config("SUPABASE_KEY")
    supabase: Client = create_client(url, key)
    for item in supabase.table('notas').select('*').eq('numero_parcial',parcial).execute().data:
        estudiante_id.append(item["estudiante_id"])
        nrc_materia.append(item["materia_nrc"])
        descripcion.append(item["nota_descripcion"])
        valor.append(item["nota_valor"])
    return estudiante_id,nrc_materia,descripcion,valor

<<<<<<< HEAD
def buscar_notas_IDEsudiante(idEstudiante: int):
    estudiante_id = []
    nrc_materia = []
    nota_final = []
    url: str = config("SUPABASE_URL")
    key: str = config("SUPABASE_KEY")
    supabase: Client = create_client(url, key)
    for item in supabase.table('notas').select('*').eq('estudiante_id',idEstudiante).execute().data:
        estudiante_id.append(item["estudiante_id"])
        nrc_materia.append(item["materia_nrc"])
        nota_final.append(item["nota_valor"])
    return estudiante_id,nrc_materia,nota_final

def buscar_id_Estudiante(idEstudiante: int):
    url: str = config("SUPABASE_URL")
    key: str = config("SUPABASE_KEY")
    supabase: Client = create_client(url, key)
    for item in supabase.table('estudiante').select('*').eq('id',idEstudiante).execute().data:
        return item["id"]

def buscar_id_nota(idNota: int):
    url: str = config("SUPABASE_URL")
    key: str = config("SUPABASE_KEY")
    supabase: Client = create_client(url, key)
    for item in supabase.table('notas').select('*').eq('id_not',idNota).execute().data:
        return item["id_not"]
=======


>>>>>>> 213f90315bdb41bdd77cbd86742d6e4218609ae9
