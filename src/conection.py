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
    
