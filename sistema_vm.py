from sede import Sede
from disenador import Disenador
from cita import Cita
from bloque_horario import BloqueHorario

class Sistema:
#Gestiona la logica de la aplicacion del sistema de citas incluyento usuarios, sedes, diseñadores, bloques de horario y agendamientos.
    def __init__(self):
        self._usuarios=[]
        self._sedes = []
        self._citas = []
        self._bloquesHorarios= []
        self.crearDatosIniciales()
        self.crearBloquesHorarios()
    #Inicializa una instancia del sistema e invoca la precarga de los datos iniciales
    
    def crearDatosIniciales(self):
        sede1 = Sede(
            1,
            "Madecentro Medellín",
            "Cra. 58 #62 74, La Candelaria, Medellín, La Candelaria, Medellín, Antioquia"
        )

        sede2 = Sede(
            2,
            "Madecentro Envigado",
            "Cl. 38 Sur #39-45, Zona 9, Envigado, Antioquia"
        )

        sede3 = Sede(
            3,
            "Madecentro Bello",
            "Cra. 50a #53 62, Andalucia, Bello, Antioquia"
        )

        disenador1 = Disenador(
            1,
            "Camilo perez",
            "camilo@visionmadera.com"
        )

        disenador2 = Disenador(
            2,
            "Brayan Alvarez",
            "Bray@visionmadera.com"
        )

        disenador3 = Disenador(
            3,
            "Andrés Garcia",
            "andres@visionmadera.com"
        )

        disenador4 = Disenador(
            4,
            "Juan Morales",
            "Juan@visionmadera.com"
        )
        #Precarga las sedes y disenadores iniciales en la memoria del sistema

        sede1.agregarDisenador(disenador1)
        sede1.agregarDisenador(disenador2)
        sede2.agregarDisenador(disenador3)
        sede3.agregarDisenador(disenador4)

        self._sedes.append(sede1)
        self._sedes.append(sede2)
        self._sedes.append(sede3)

    def registrarUsuario(self, usuario):
        usuarioDocumento= self.buscarUsuarioDocumento(usuario.documento)
        if usuarioDocumento != None:
            return False
        usuarioEmail= self.buscarUsuarioEmail(usuario.email)
        if usuarioEmail != None:
            return False
        self._usuarios.append(usuario)
        return True 
    #Registra un nuevo usuario validando que si documento y correo no este ya registrado en el sistema
        
    def buscarUsuarioEmail(self, email):
        for usuario in self._usuarios:
            if usuario.email == email:
                return usuario
        return None
    #Busca un usuario en el sistema segun su direccion de correo electronico
    
    def buscarUsuarioDocumento(self, documento):
        for usuario in self._usuarios:
            if usuario.documento==documento:
                return usuario
        return None
    #Busca un usuario en el sistema segun su documento
    
    def listarUsuarios(self):
        for usuario in self._usuarios:
            usuario.mostrarInformacion()
    #Imprime por consola todos los usuarios registrados en el sistema (No implementado en el momento)
            
    def eliminarUsuario(self, documento):
        usuario= self.buscarUsuarioDocumento(documento)
        if usuario != None:
            self._usuarios.remove(usuario)
            return True
        return False
    #Remueve un usuario mediante su documento (No implementado en el momento)
    
    def iniciarSesion(self, email, contrasena):
        usuario= self.buscarUsuarioEmail(email)
        if usuario != None:
            if usuario.verificarContrasena(contrasena):
                return usuario
        return None
    #Autenticacion de las credenciales del usuario apara acceder al sistema
    
    def mostrarSedes(self):
        print("\n===== PUNTOS DE VENTA =====")
        for sede in self._sedes:
            print(
                f"{sede.idSede}. "
                f"{sede.nombre} - "
                f"{sede.direccion}"
            )
    #Imprime por consola la lista de las sedes disponibles
    
    def mostrarDisenadores(self, sede):
        print("\n===== DISEÑADORES DISPONIBLES =====")
        for disenador in sede.disenadores:
            print(
                f"{disenador.idDisenador}. "
                f"{disenador.nombre}"
            )
    #Imprime por consola la lista de diseñadores disponibles asociados a una sede en particular

    def agendarCita(self, usuario, sede, disenador, fecha, bloqueHorario):
        for cita in self._citas:
            if (
                cita.disenador== disenador
                and cita.fecha== fecha
                and cita.bloqueHorario== bloqueHorario
            ):
                return None
        cita = Cita(
            usuario,
            sede,
            disenador,
            fecha,
            bloqueHorario
        )
        self._citas.append(cita)
        return cita
    #Crea un agendamiento de cita y lo guarda en el sistema tras verificar disponibilidad.
    
    def buscarSede(self, idSede):
        for sede in self._sedes:
            if str(sede.idSede) == str(idSede):
                return sede
        return None
    #Busca una sede por su id
    
    def buscarDisenador(self, sede, idDisenador):
        for disenador in sede.disenadores:
            if str(disenador.idDisenador) == str(idDisenador):
                return disenador
        return None
    #Busca un diseñador dentro de la lista de una sede especifica segun su id
    
    def mostrarMisCitas(self, usuario):
        tieneCitas = False
        print("\n==========================")
        print("       MIS CITAS")
        print("==========================")
        for cita in self._citas:
            if cita.usuario == usuario:
                cita.mostrarInformacion()
                tieneCitas = True
        if tieneCitas == False:
            print("\nNo tienes citas agendadas.")
    #Muestra en consola las citas agendadas por un usuario determinado
            
    def obtenerMisCitas(self, usuario):
        return [cita for cita in self._citas if cita.usuario == usuario]
    #Filtra y retorna la lista de citas agendadas correspondientes a un usuario

    def modificarMisCitas(
        self,
        usuario,
        numeroCita,
        sede=None,
        disenador=None,
        fecha=None,
        bloqueHorario=None
    ):
        citasUsuario = self.obtenerMisCitas(usuario)
        if numeroCita < 1 or numeroCita > len(citasUsuario):
            return False
        cita = citasUsuario[numeroCita - 1]
        nuevaSede = sede if sede is not None else cita.sede
        nuevoDisenador = (
            disenador if disenador is not None else cita.disenador
        )
        nuevaFecha= fecha if fecha is not None else cita.fecha
        nuevoBloqueHorario= (
            bloqueHorario if bloqueHorario is not None else cita.bloqueHorario
        )
        if nuevoDisenador not in nuevaSede.disenadores:
            return False
        for otraCita in self._citas:
            if (
                otraCita != cita
                and otraCita.disenador== nuevoDisenador
                and otraCita.fecha== nuevaFecha
                and otraCita.bloqueHorario== nuevoBloqueHorario
            ):
                return False
        cita.sede = nuevaSede
        cita.disenador = nuevoDisenador
        cita.fecha = nuevaFecha
        cita.bloqueHorario= nuevoBloqueHorario
        return True
    #Modifica los datos de una cita existente para un usuario validado que no existan horarios duplicados
    
    def cancelarCita(self, usuario, numeroCita):
        citasUsuario = self.obtenerMisCitas(usuario)
        if numeroCita < 1 or numeroCita > len(citasUsuario):
            return False
        cita = citasUsuario[numeroCita - 1]
        self._citas.remove(cita)
        return True
    #Cancela y remueve una cita del sistema
    
    def crearBloquesHorarios(self):
        bloque1= BloqueHorario(1, "08:00", "10:00")
        bloque2= BloqueHorario(2, "10:00", "12:00")
        bloque3= BloqueHorario(3, "12:00", "14:00")
        bloque4= BloqueHorario(4, "14:00", "16:00")
        bloque5= BloqueHorario(5, "16:00", "18:00")
        bloque6= BloqueHorario(6, "18:00", "20:00")
        
        self._bloquesHorarios.append(bloque1)
        self._bloquesHorarios.append(bloque2)
        self._bloquesHorarios.append(bloque3)
        self._bloquesHorarios.append(bloque4)
        self._bloquesHorarios.append(bloque5)
        self._bloquesHorarios.append(bloque6)
    #Instancia y almacena los bloques horarios en la lista de bloqueshorarios
        
    def mostrarBloquesHorarios(self):
        print("\n===== HORARIOS DISPONIBLES =====")
        for bloque in self._bloquesHorarios:
            bloque.mostrarInformacion()
    #Imprime por consola la lista de los bloques horarios disponibles
            
    def buscarBloqueHorario(self, idBloque):
        for bloque in self._bloquesHorarios:
            if str(bloque.idBloque) == str(idBloque):
                return bloque
        return None
    #Busca una elemento de la lista bloqueshorarios por su id