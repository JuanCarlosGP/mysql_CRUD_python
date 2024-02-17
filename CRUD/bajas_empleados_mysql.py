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

def eliminar_empleado(conexion, codigo_empleado, archivos_output):
    cursor = conexion.cursor()
    query = "DELETE FROM mae_empleados WHERE codigo = %s"
    try:
        cursor.execute(query, (codigo_empleado,))
        if cursor.rowcount == 0:
            archivos_output['fallidas'].write(codigo_empleado + '\n')
            print(f"No se encontró el empleado con código {codigo_empleado} para eliminar.")
        else:
            conexion.commit()
            archivos_output['realizadas'].write(codigo_empleado + '\n')
            print(f"Empleado con código {codigo_empleado} eliminado exitosamente.")
    except Error as e:
        print(f"El error '{e}' ocurrió al intentar eliminar el empleado con código {codigo_empleado}.")
    finally:
        cursor.close()

def leer_y_eliminar_empleados(conexion, ruta_archivo):
    with open(ruta_archivo, 'r') as archivo, \
         open('../mysql_CRUD_py/Output/Delete/bajas_correctas_mysql.txt', 'w') as realizadas, \
         open('../mysql_CRUD_py/Output/Delete/bajas_erroneas_mysql.txt', 'w') as fallidas:
        archivos_output = {'realizadas': realizadas, 'fallidas': fallidas}
        for linea in archivo:
            codigo_empleado = linea.strip()
            eliminar_empleado(conexion, codigo_empleado, archivos_output)

if __name__ == "__main__":
    load_dotenv()
    conexion = bd.crear_conexion()
    if conexion is not None:
        ruta_archivo = '../mysql_CRUD_py/Input/Delete/bajas_mysql.txt'
        leer_y_eliminar_empleados(conexion, ruta_archivo)
        conexion.close()
    else:
        print("No se pudo establecer la conexión a la base de datos.")
