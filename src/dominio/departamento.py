from dominio.empleado import Empleado

class Departamento:
    def _unit(self, nombre: str):
        self.nombre = nombre
        self._empleados: list[Empleado] = []

    def agregar_empleado(self, empleado: Empleado) -> bool:
        if empleado in self._empleados:
            return False

        self.empleados.append(empleado)
        return True