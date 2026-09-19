class Cita:
    #Representa un cita agendada entre un usuario y un diseñador
    def __init__(self, usuario, sede, disenador, fecha, bloqueHorario):
        self._usuario = usuario
        self._sede = sede
        self._disenador = disenador
        self._fecha = fecha
        self._bloqueHorario = bloqueHorario
    #Instancia de la clase cita 

    @property
    def usuario(self):
        return self._usuario
    #Obtiene el usuario asociado a la cita

    @property
    def sede(self):
        return self._sede
    #Obtiene o establece la sede de la cita

    @sede.setter
    def sede(self, valor):
        self._sede = valor

    @property
    def disenador(self):
        return self._disenador
    #Obtiene o establece el diseñador asignado a la cita

    @disenador.setter
    def disenador(self, valor):
        self._disenador = valor

    @property
    def fecha(self):
        return self._fecha
    #Obtiene o establece la fecha de la cita
    
    @fecha.setter
    def fecha(self, valor):
        self._fecha = valor
        
    @property
    def bloqueHorario(self):
        return self._bloqueHorario
    #Obtiene o establece el bloque horario de la cita
    
    @bloqueHorario.setter
    def bloqueHorario(self, valor):
        self._bloqueHorario = valor

    def mostrarInformacion(self):
        print("\n===== INFORMACIÓN DE LA CITA =====")
        print(f"Usuario: {self._usuario.nombre}")
        print(f"Sede: {self._sede.nombre}")
        print(f"Dirección: {self._sede.direccion}")
        print(f"Diseñador: {self._disenador.nombre}")
        print(f"Fecha: {self._fecha}")
        print(
            f"Horario: {self._bloqueHorario.horaInicio} - "
            f"{self._bloqueHorario.horaFin}"
        )
    #Imprime por consola los detalles principales de la cita