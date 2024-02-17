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

def insertar_empleado(conexion, empleado, archivos_output):
    cursor = conexion.cursor()
    query = """
    INSERT INTO mae_empleados (codigo, nombre, apellidos, nif, departamento, num_hijos)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    try:
        cursor.execute(query, empleado)
        conexion.commit()
        archivos_output['correctos'].write(';'.join(map(str, empleado)) + '\n')
        print("Empleado insertado exitosamente")
    except Error as e:
        if e.errno == 1062:  # Código de error para duplicados en MySQL
            archivos_output['erroneos'].write(';'.join(map(str, empleado)) + '\n')
            print(f"El empleado con código {empleado[0]} ya existe.")
        else:
            print(f"El error '{e}' ocurrió")
    finally:
        cursor.close()

def verificar_y_crear_tabla(conexion):
    cursor = conexion.cursor()
    create_table_query = """
    CREATE TABLE IF NOT EXISTS `mae_empleados` (
        `codigo` VARCHAR(4) NOT NULL,
        `nombre` VARCHAR(30) NOT NULL,
        `apellidos` VARCHAR(45) NOT NULL,
        `nif` VARCHAR(9) NOT NULL,
        `departamento` VARCHAR(15) NOT NULL,
        `num_hijos` INT NOT NULL,
        PRIMARY KEY(`codigo`)
    ) ENGINE=InnoDB;
    """
    try:
        cursor.execute(create_table_query)
        conexion.commit()
        print("La tabla 'mae_empleados' fue creada exitosamente.")
    except Error as e:
        print(f"El error '{e}' ocurrió al crear la tabla.")
    finally:
        cursor.close()

def leer_y_insertar_empleados(conexion, ruta_archivo):
    with open(ruta_archivo, 'r') as archivo, \
         open('../mysql_CRUD_py/Output/Create/altas_correctas_mysql.txt', 'w') as correctos, \
         open('../mysql_CRUD_py/Output/Create/altas_erroneas_mysql.txt', 'w') as erroneos:
        archivos_output = {'correctos': correctos, 'erroneos': erroneos}
        for linea in archivo:
            datos = linea.strip().split(';')
            if len(datos) == 6:
                insertar_empleado(conexion, datos, archivos_output)
            else:
                erroneos.write(linea)
                print(f"Error en la línea: {linea}. Datos incompletos.")

def insertar_empleado_especifico(conexion):
    empleado_especifico = ('0001', 'Juan', 'García García', '12345678Z', 'Contabilidad', 2)
    with open('../mysql_CRUD_py/Output/Create/altas_correctas_mysql.txt', 'a') as correctos, \
         open('../mysql_CRUD_py/Output/Create/altas_erroneas_mysql.txt', 'a') as erroneos:
        archivos_output = {'correctos': correctos, 'erroneos': erroneos}
        insertar_empleado(conexion, empleado_especifico, archivos_output)

if __name__ == "__main__":
    load_dotenv()
    conexion = bd.crear_conexion()
    if conexion is not None:
        verificar_y_crear_tabla(conexion)
        ruta_archivo = '../mysql_CRUD_py/Input/Create/altas_mysql.txt'
        leer_y_insertar_empleados(conexion, ruta_archivo)
        # Para NO insertar un error, comentar la líne inferior
        #insertar_empleado_especifico(conexion)
        conexion.close()
    else:
        print("No se pudo establecer la conexión a la base de datos.")
