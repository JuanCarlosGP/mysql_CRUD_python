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

def volcar_datos_empleados(conexion, ruta_archivo_salida):
    cursor = conexion.cursor()
    query = "SELECT codigo, nombre, apellidos, nif, departamento, num_hijos FROM mae_empleados"
    try:
        cursor.execute(query)
        empleados = cursor.fetchall()
        with open(ruta_archivo_salida, 'w') as archivo:
            for empleado in empleados:
                linea = ';'.join(map(str, empleado)) + '\n'
                archivo.write(linea)
        print("Todos los datos de empleados han sido volcados al archivo correctamente.")
    except Error as e:
        print(f"El error '{e}' ocurrió al intentar leer los datos de los empleados.")
    finally:
        cursor.close()

if __name__ == "__main__":
    load_dotenv()
    conexion = bd.crear_conexion()
    if conexion is not None:
        ruta_archivo_salida = '../mysql_CRUD_py/Output/Read/consulta_mysql.txt'
        volcar_datos_empleados(conexion, ruta_archivo_salida)
        conexion.close()
    else:
        print("No se pudo establecer la conexión a la base de datos.")
