from gettext import find
from tokenize import Double
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
    data = supabase.table("materia").select("nrc").execute().json()
    data = re.findall('[0-9]+',data)
    return data

def insert_nota(id: int, estudiante: str, nrc: int, nota: float, descripcion: str, parcial: int):
    url: str = config("SUPABASE_URL")
    key: str = config("SUPABASE_KEY")
    supabase: Client = create_client(url, key)
    data = supabase.table("notas").insert({"id_not": id, "estudiante_id": estudiante, "materia_nrc": nrc, "nota_valor": nota, "nota_descripcion": descripcion, "numero_parcial": parcial}).execute()
    
    
    
