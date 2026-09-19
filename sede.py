class Sede:
    #Representa una sede fisica donde se prestan servicios de diseño y atencion
    def __init__(self, idSede, nombre, direccion):
        self._idSede = idSede
        self._nombre = nombre
        self._direccion = direccion
        self._disenadores = []
    #Instancia de la clase sede
        
    @property
    def idSede(self):
        return self._idSede
    #Obtiene el identificador único de la sede

    @property
    def nombre(self):
        return self._nombre
    #Obtiene el nombre de la sede
    
    @property
    def direccion(self):
        return self._direccion
    #Obtiene la dirección física de la sede

    @property
    def disenadores(self):
        return self._disenadores
    #Obtiene la lista de diseñadores asociados a la sede

    def agregarDisenador(self, disenador):
        self._disenadores.append(disenador)
        #Agrega un nuevo diseñador a la lista de personal asignado a esta sede
        
    def mostrarInformacion(self):
        print(f"Sede: {self._nombre}")
        print(f"Dirección: {self._direccion}")
        #Imprime en consola la información básica de la sede