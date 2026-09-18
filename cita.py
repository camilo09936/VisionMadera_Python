class Cita:

    def __init__(self, usuario, sede, disenador, fecha):
        self._usuario = usuario
        self._sede = sede
        self._disenador = disenador
        self._fecha = fecha

    @property
    def usuario(self):
        return self._usuario

    @property
    def sede(self):
        return self._sede

    @sede.setter
    def sede(self, valor):
        self._sede = valor

    @property
    def disenador(self):
        return self._disenador

    @disenador.setter
    def disenador(self, valor):
        self._disenador = valor

    @property
    def fecha(self):
        return self._fecha
    
    @fecha.setter
    def fecha(self, valor):
        self._fecha = valor

    def mostrarInformacion(self):
        print("\n===== INFORMACIÓN DE LA CITA =====")
        print(f"Usuario: {self._usuario.nombre}")
        print(f"Sede: {self._sede.nombre}")
        print(f"Dirección: {self._sede.direccion}")
        print(f"Diseñador: {self._disenador.nombre}")
        print(f"Fecha: {self._fecha}")