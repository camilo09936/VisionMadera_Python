class Sede:

    def __init__(self, idSede, nombre, direccion):
        self._idSede = idSede
        self._nombre = nombre
        self._direccion = direccion
        self._disenadores = []

    @property
    def idSede(self):
        return self._idSede

    @property
    def nombre(self):
        return self._nombre

    @property
    def direccion(self):
        return self._direccion

    @property
    def disenadores(self):
        return self._disenadores

    def agregarDisenador(self, disenador):
        self._disenadores.append(disenador)

    def mostrarInformacion(self):
        print(f"Sede: {self._nombre}")
        print(f"Dirección: {self._direccion}")