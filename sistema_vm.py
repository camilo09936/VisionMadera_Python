from sede import Sede
from disenador import Disenador
from cita import Cita

class Sistema:

    def __init__(self):
        self._usuarios=[]
        self._sedes = []
        self._citas = []
        self.crearDatosIniciales()
        
    def crearDatosIniciales(self):
        sede1 = Sede(
            1,
            "Madecentro Medellín",
            "Dirección sede Medellín"
        )

        sede2 = Sede(
            2,
            "Madecentro Envigado",
            "Dirección sede Envigado"
        )

        sede3 = Sede(
            3,
            "Madecentro Bello",
            "Dirección sede Bello"
        )

        disenador1 = Disenador(
            1,
            "Carlos Gómez",
            "carlos@visionmadera.com"
        )

        disenador2 = Disenador(
            2,
            "María Rodríguez",
            "maria@visionmadera.com"
        )

        disenador3 = Disenador(
            3,
            "Andrés López",
            "andres@visionmadera.com"
        )

        disenador4 = Disenador(
            4,
            "Laura Martínez",
            "laura@visionmadera.com"
        )

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
        
    def buscarUsuarioEmail(self, email):
        for usuario in self._usuarios:
            if usuario.email == email:
                return usuario
        return None
    
    def buscarUsuarioDocumento(self, documento):
        for usuario in self._usuarios:
            if usuario.documento==documento:
                return usuario
        return None
    
    def listarUsuarios(self):
        for usuario in self._usuarios:
            usuario.mostrarInformacion()
            
    def eliminarUsuario(self, email):
        usuario= self.buscarUsuarioEmail(email)
        if usuario != None:
            self._usuarios.remove(usuario)
            return True
        return False
    
    def iniciarSesion(self, email, contrasena):
        usuario= self.buscarUsuarioEmail(email)
        if usuario != None:
            if usuario.verificarContrasena(contrasena):
                return usuario
        return None
    
    def mostrarSedes(self):
        print("\n===== PUNTOS DE VENTA =====")
        for sede in self._sedes:
            print(
                f"{sede.idSede}. "
                f"{sede.nombre} - "
                f"{sede.direccion}"
            )
    
    def mostrarDisenadores(self, sede):
        print("\n===== DISEÑADORES DISPONIBLES =====")
        for disenador in sede.disenadores:
            print(
                f"{disenador.idDisenador}. "
                f"{disenador.nombre}"
            )

    def agendarCita(self, usuario, sede, disenador, fecha):
        cita = Cita(
            usuario,
            sede,
            disenador,
            fecha
        )
        self._citas.append(cita)
        return cita