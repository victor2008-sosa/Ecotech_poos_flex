from percistencia.conexion import abrir_conexion, obtener_motor
from dominio.empleado import Empleado


class EmpleadoDAO:
    @staticmethod
    def insertar(empleado):
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        marcador = "?" if obtener_motor() == "sqlite" else "%s"

        sql = f"""
        INSERT INTO empleado (nombre, correo)
        VALUES ({marcador}, {marcador})
        """
        cursor.execute(sql, (empleado.nombre, empleado.correo))
        empleado.id = cursor.lastrowid
        conexion.commit()
        conexion.close()
        return empleado

    def listar():
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        sql = (
            "SELECT id, nombre, correo "
            "FROM empleado ORDER BY id"
        )
        cursor.execute(sql)
        filas = cursor.fetchall()
        empleados = []
        for id_empleado, nombre, correo in filas:
            empleado = Empleado(
                nombre=nombre, correo=correo, id=id_empleado
            )  
            empleados.append(empleado)
        return empleados