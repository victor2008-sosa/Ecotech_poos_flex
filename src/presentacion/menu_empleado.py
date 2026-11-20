import sqlite3
import pymysql
from dominio.empleado import Empleado
from percistencia.empleado_dao import EmpleadoDAO

# Agrupamos las excepciones reales de ambos motores de base de datos
ERRORES_INTEGRIDAD = (sqlite3.IntegrityError, pymysql.err.IntegrityError)
ERRORES_BD = (sqlite3.Error, pymysql.MySQLError)


def solicitar_nombre() -> str:
    while True:
        valor = input("Nombre: ")
        try:
            return Empleado.validar_nombre(valor)
        except ValueError as error:
            print(f"Nombre inválido: {error}")


def solicitar_correo() -> str:
    while True:
        valor = input("Correo: ")
        try:
            return Empleado.validar_correo(valor)
        except ValueError as error:
            print(f"Correo inválido: {error}")


def solicitar_id() -> int:
    while True:
        texto = input("ID del empleado: ").strip()
        try:
            id_empleado = int(texto)
            if id_empleado <= 0:
                raise ValueError("El ID debe ser positivo.")
            return id_empleado
        except ValueError:
            print("Ingresa un entero mayor que 0.")


def crear_empleado():
    nombre = solicitar_nombre()
    correo = solicitar_correo()
    try:
        empleado = Empleado(nombre=nombre, correo=correo)
        EmpleadoDAO.insertar(empleado)
        print(f"Empleado registrado. ID: {empleado.id}")
    except ERRORES_INTEGRIDAD:
        print("Ese correo ya está registrado.")
    except ERRORES_BD as error:
        print("No se pudo acceder a la base de datos:", error)


def listar_empleados():
    try:
        empleados = EmpleadoDAO.listar()
        if not empleados:
            print("Todavía no hay empleados registrados.")
        else:
            for empleado in empleados:
                print(f"{empleado.id}: {empleado.nombre} - {empleado.correo}")
    except ERRORES_BD as error:
        print("No se pudo acceder a la base de datos:", error)


def buscar_empleado():
    id_empleado = solicitar_id()
    try:
        empleado = EmpleadoDAO.buscar_por_id(id_empleado)
        if empleado is None:
            print("No existe un empleado con ese ID.")
        else:
            print(f"{empleado.id}: {empleado.nombre} - {empleado.correo}")
    except ERRORES_BD as error:
        print("No se pudo acceder a la base de datos:", error)


def actualizar_empleado():
    id_empleado = solicitar_id()
    try:
        empleado = EmpleadoDAO.buscar_por_id(id_empleado)
        if empleado is None:
            print("No existe un empleado con ese ID.")
            return
        nuevo_correo = solicitar_correo()
        if nuevo_correo == empleado.correo:
            print("El correo es el mismo; no hay cambios.")
            return
        empleado.correo = nuevo_correo
        filas = EmpleadoDAO.actualizar(empleado)
        if filas == 1:
            print("Correo actualizado correctamente.")
        else:
            print("Vuelve a consultar el estado del empleado.")
    except ERRORES_INTEGRIDAD:
        print("Ese correo ya está registrado.")
    except ERRORES_BD as error:
        print("No se pudo acceder a la base de datos:", error)


def eliminar_empleado():
    id_empleado = solicitar_id()
    try:
        empleado = EmpleadoDAO.buscar_por_id(id_empleado)
        if empleado is None:
            print("No existe un empleado con ese ID.")
            return
        print(f"Seleccionado: {empleado.id}: {empleado.nombre} - {empleado.correo}")
        confirmacion = input("¿Confirmas eliminar este empleado? (s/n): ").strip().lower()
        if confirmacion != "s":
            print("Eliminación cancelada.")
            return
        filas = EmpleadoDAO.eliminar(id_empleado)
        if filas == 1:
            print("Empleado eliminado correctamente.")
    except ERRORES_BD as error:
        print("No se pudo acceder a la base de datos:", error)


def menu_empleados():
    while True:
        print("\n1. Registrar \n2. Listar \n3. Buscar por ID \n4. Actualizar correo \n5. Eliminar \n0. Salir")
        opcion = input("Opción: ").strip()
        if opcion == "1":
            crear_empleado()
        elif opcion == "2":
            listar_empleados()
        elif opcion == "3":
            buscar_empleado()
        elif opcion == "4":
            actualizar_empleado()
        elif opcion == "5":
            eliminar_empleado()
        elif opcion == "0":
            break
        else:
            print("Elige una opción válida (0 a 5).")