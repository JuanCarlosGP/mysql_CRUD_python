from dotenv import load_dotenv
import os
import mysql.connector
from mysql.connector import Error

import sys
from pathlib import Path
current_dir = Path(__file__).parent
conexion_dir = current_dir.parent / 'conexion_file'
sys.path.append(str(conexion_dir))
import conexion_bbdd as bd


def insertar_empleado(conexion, empleado):
    cursor = conexion.cursor()
    query = """
    INSERT INTO mae_empleados (codigo, nombre, apellidos, nif, departamento, num_hijos)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    try:
        cursor.execute(query, empleado)
        conexion.commit()
        print("Empleado insertado exitosamente")
    except Error as e:
        print(f"El error '{e}' ocurrió")

def leer_y_insertar_empleados(ruta_archivo):
    # Cargar las variables de entorno y crear conexión
    load_dotenv()
    conexion = bd.crear_conexion()

    if conexion is not None:
        with open(ruta_archivo, 'r') as archivo:
            for linea in archivo:
                datos = linea.strip().split(';')
                # Asegúrate de que los datos estén completos antes de intentar insertar
                if len(datos) == 6:
                    insertar_empleado(conexion, datos)
                else:
                    print(f"Error en la línea: {linea}. Datos incompletos.")
        # Cerrar la conexión a la base de datos
        conexion.close()
    else:
        print("No se pudo establecer la conexión a la base de datos.")

# Ruta al archivo de texto
ruta_archivo = 'D:/GestionEmpresarial/mysql_CRUD_py/Input/Create/altas_mysql.txt'
leer_y_insertar_empleados(ruta_archivo)
