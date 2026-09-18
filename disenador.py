class Disenador:

    def __init__(self, idDisenador, nombre, correo):
        self._idDisenador = idDisenador
        self._nombre = nombre
        self._correo = correo

    @property
    def idDisenador(self):
        return self._idDisenador

    @property
    def nombre(self):
        return self._nombre

    @property
    def correo(self):
        return self._correo

    def mostrarInformacion(self):
        print(f"Nombre: {self._nombre}")
        print(f"Correo: {self._correo}")