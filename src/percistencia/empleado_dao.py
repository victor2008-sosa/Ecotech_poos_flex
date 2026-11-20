from percistencia.conexion import abrir_conexion, obtener_motor
from dominio.empleado import Empleado


class EmpleadoDAO:
    @staticmethod
    def _obtener_marcador():
        """Método auxiliar privado para no repetir esta lógica en cada consulta."""
        return "?" if obtener_motor() == "sqlite" else "%s"

    # C - CREATE (Crear)
    @staticmethod
    def insertar(empleado):
        conexion = abrir_conexion()
        try:
            cursor = conexion.cursor()
            marcador = EmpleadoDAO._obtener_marcador()
            sql = f"INSERT INTO empleado (nombre, correo) VALUES ({marcador}, {marcador})"
            
            cursor.execute(sql, (empleado.nombre, empleado.correo))
            empleado.id = cursor.lastrowid
            conexion.commit()
            return empleado
        finally:
            conexion.close()

    # R - READ (Leer todos)
    @staticmethod
    def listar():
        conexion = abrir_conexion()
        try:
            cursor = conexion.cursor()
            sql = "SELECT id, nombre, correo FROM empleado ORDER BY id"
            cursor.execute(sql)
            filas = cursor.fetchall()
            
            empleados = []
            for id_empleado, nombre, correo in filas:
                empleados.append(Empleado(nombre=nombre, correo=correo, id=id_empleado))
            return empleados
        finally:
            conexion.close()

    # R - READ (Leer uno solo por ID)
    @staticmethod
    def buscar_por_id(id_empleado):
        conexion = abrir_conexion()
        try:
            cursor = conexion.cursor()
            marcador = EmpleadoDAO._obtener_marcador()
            sql = f"SELECT id, nombre, correo FROM empleado WHERE id = {marcador}"
            
            cursor.execute(sql, (id_empleado,))
            fila = cursor.fetchone()
            
            if fila:
                return Empleado(id=fila[0], nombre=fila[1], correo=fila[2])
            return None
        finally:
            conexion.close()

    # U - UPDATE (Actualizar)
    @staticmethod
    def actualizar(empleado):
        conexion = abrir_conexion()
        try:
            cursor = conexion.cursor()
            marcador = EmpleadoDAO._obtener_marcador()
            sql = f"""
            UPDATE empleado 
            SET nombre = {marcador}, correo = {marcador} 
            WHERE id = {marcador}
            """
            cursor.execute(sql, (empleado.nombre, empleado.correo, empleado.id))
            conexion.commit()
            return cursor.rowcount
        finally:
            conexion.close()

    # D - DELETE (Eliminar)
    @staticmethod
    def eliminar(id_empleado):
        conexion = abrir_conexion()
        try:
            cursor = conexion.cursor()
            marcador = EmpleadoDAO._obtener_marcador()
            sql = f"DELETE FROM empleado WHERE id = {marcador}"
            
            cursor.execute(sql, (id_empleado,))
            conexion.commit()
            return cursor.rowcount
        finally:
            conexion.close()