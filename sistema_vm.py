class Sistema:
    def __init__(self):
        self._usuarios=[]
        
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