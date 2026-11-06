from dominio.empleado import  Empleado
from dominio.departamento import Departamento
from percistencia.empleado_dao import EmpleadoDAO
from percistencia.creacion_bd import crear_tablas
crear_tablas()

emp = Empleado("correo@gmail.cl","juanito")
print(emp)
EmpleadoDAO.insertar(emp)
print(emp.mostrar_datos())
