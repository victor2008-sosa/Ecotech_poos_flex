from dominio.empleado import  Empleado
from dominio.departamento import Departamento
from percistencia.empleado_dao import EmpleadoDAO
from percistencia.creacion_bd import crear_tablas
crear_tablas()



try:
    empleado = Empleado("juanito"" ", "ana@ecotech.cl")
except ValueError as error:
    print(f"No se pudo crear el empleado: {error}")
else:
    print(f"Datos válidos: {empleado.nombre}")
EmpleadoDAO.insertar(empleado)
empleados = EmpleadoDAO.listar()

if not empleados:
    print("Todavía no hay empleados registrados.")
else:
    for empleado in empleados:
        print(
            f"{empleado.id}: {empleado.nombre} "
            f"- {empleado.correo}"
        )