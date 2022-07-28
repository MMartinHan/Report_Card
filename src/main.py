from decouple import config
from supabase import create_client, Client

url: str = config("SUPABASE_URL")
key: str = config("SUPABASE_KEY")
supabase: Client = create_client(url, key)
nombre= input("Ingrese el nombre:")
apellido= input("Ingrese el apellido:")
nombre=nombre.upper()
print(nombre)
apellido=apellido.upper()
print(apellido)
data = supabase.table("estudiante").insert({"id":"1","first_name":nombre,"last_name":apellido}).execute()
