from dotenv import load_dotenv
import os
import mysql.connector
from mysql.connector import Error
# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Acceder a las variables de entorno
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

# Usar estas variables para crear la conexión
def crear_conexion():
    conexion = None
    try:
        conexion = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            passwd=DB_PASSWORD,
            database=DB_NAME
        )
        print("Conexión a MySQL DB exitosa")
    except Error as e:
        print(f"El error '{e}' ocurrió")

    return conexion
