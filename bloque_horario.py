class BloqueHorario:
#Representa los bloques de horario disponibles para la programacion de cita.
    def __init__(self, idBloque, horaInicio, horaFin):
        self._idBloque = idBloque
        self._horaInicio = horaInicio
        self._horaFin = horaFin
#Instancia de la clase BloqueHorario
        
    @property
    def idBloque(self):
        return self._idBloque
    #Obtiene el identificador único del bloque horario
    
    @property
    def horaInicio(self):
        return self._horaInicio
    #Obtiene la hora de inicio del bloque horario
    
    @property
    def horaFin(self):
        return self._horaFin
    #Obtiene la hora de finalización del bloque horario
    def mostrarInformacion(self):
        print(
            f"{self._idBloque}. "
            f"{self._horaInicio} - {self._horaFin}"
        )
    #Imprime en consola los horarios de los bloques disponibles(HoraInicio-HoraFin)