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

def modificar_empleado(conexion, empleado, archivos_output):
    cursor = conexion.cursor()
    query = """
    UPDATE mae_empleados
    SET nombre = %s, apellidos = %s, nif = %s, departamento = %s, num_hijos = %s
    WHERE codigo = %s
    """
    try:
        cursor.execute(query, (empleado[1], empleado[2], empleado[3], empleado[4], empleado[5], empleado[0]))
        if cursor.rowcount == 0:
            archivos_output['fallidas'].write(';'.join(map(str, empleado)) + '\n')
            print(f"No se encontró el empleado con código {empleado[0]} para modificar.")
        else:
            conexion.commit()
            archivos_output['realizadas'].write(';'.join(map(str, empleado)) + '\n')
            print(f"Empleado con código {empleado[0]} modificado exitosamente.")
    except Error as e:
        print(f"El error '{e}' ocurrió al intentar modificar el empleado con código {empleado[0]}.")
    finally:
        cursor.close()

def leer_y_modificar_empleados(conexion, ruta_archivo):
    with open(ruta_archivo, 'r') as archivo, \
         open('../mysql_CRUD_py/Output/Update/modificaciones_correctas_mysql.txt', 'w') as realizadas, \
         open('../mysql_CRUD_py/Output/Update/modificaciones_erroneas_mysql.txt', 'w') as fallidas:
        archivos_output = {'realizadas': realizadas, 'fallidas': fallidas}
        for linea in archivo:
            empleado = linea.strip().split(';')
            if len(empleado) == 6:
                modificar_empleado(conexion, empleado, archivos_output)
            else:
                fallidas.write(linea)
                print(f"Error en la línea: {linea}. Datos incompletos.")

if __name__ == "__main__":
    load_dotenv()
    conexion = bd.crear_conexion()
    if conexion is not None:
        ruta_archivo = '../mysql_CRUD_py/Input/Update/modificaciones_mysql.txt'
        leer_y_modificar_empleados(conexion, ruta_archivo)
        conexion.close()
    else:
        print("No se pudo establecer la conexión a la base de datos.")
