class Empleado:
    MIN_NOMBRE = 2
    MAX_NOMBRE = 80
    MIN_CORREO = 5
    MAX_CORREO = 150

    def __init__(self, nombre, correo, id=None):
        self.id = id
        self.nombre = nombre
        self.correo = correo

    def mostrar_datos(self) -> str:
        return f"{self.nombre} - {self.correo}"

    @staticmethod
    def validar_nombre(nombre):
        if not isinstance(nombre, str):
            raise ValueError("El nombre debe ser texto.")
        nombre = nombre.strip()
        if not (Empleado.MIN_NOMBRE <= len(nombre)
                <= Empleado.MAX_NOMBRE):
            raise ValueError(
                "El nombre debe tener entre 2 y 80 caracteres."
            )
        return nombre


    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = self.validar_nombre(valor)
