class Disenador:
    #Representa al diseñanor que atendera la cita
    def __init__(self, idDisenador, nombre, correo):
        self._idDisenador = idDisenador
        self._nombre = nombre
        self._correo = correo
    #Instancia de la clase diseñaor

    @property
    def idDisenador(self):
        return self._idDisenador
    #Obtiene el identificador único del diseñador

    @property
    def nombre(self):
        return self._nombre
    #Obtiene el nombre del diseñador

    @property
    def correo(self):
        return self._correo
    #Obtiene el correo electrónico del diseñador

    def mostrarInformacion(self):
        print(f"Nombre: {self._nombre}")
        print(f"Correo: {self._correo}")
    #Imprime en consola los datos básicos del diseñador