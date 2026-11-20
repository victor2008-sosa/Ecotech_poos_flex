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

    @staticmethod
    def validar_correo(correo: str) -> str:
        if not isinstance(correo, str):
            raise ValueError("El correo debe ser texto.")
        correo = correo.strip()
        if not (Empleado.MIN_CORREO <= len(correo) <= Empleado.MAX_CORREO):
            raise ValueError("El correo debe tener entre 5 y 150 caracteres.")
        if " " in correo or correo.count("@") != 1:
            raise ValueError("El correo debe tener un solo @ y evitar espacios internos.")
        usuario, dominio = correo.split("@")
        if not usuario or "." not in dominio:
            raise ValueError("El correo requiere usuario y dominio con punto.")
        partes_dominio = dominio.split(".")
        if any(not parte for parte in partes_dominio):
            raise ValueError("El dominio no puede tener partes vacías.")
        return correo

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = self.validar_nombre(valor)
