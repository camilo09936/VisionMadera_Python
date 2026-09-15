class Usuario:
    def __init__(self, documento, nombre, email, contrasena, fechaNacimiento, direccion, telefono):
        self._documento=documento #Documento Protegido
        self.nombre=nombre
        self.email=email
        self.__contrasena=contrasena #Contraseña privada (acceible solo con métodos)
        self.fechaNacimiento=fechaNacimiento
        self.direccion=direccion
        self.telefono=telefono
        
    @property
    def documento(self):
        return self._documento
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor
        
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, valor):
        self._email = valor
        
    @property
    def fechaNacimiento(self):
        return self._fechaNacimiento
    
    @fechaNacimiento.setter
    def fechaNacimiento(self, valor):
        self._fechaNacimiento = valor
        
    @property
    def direccion(self):
        return self._direccion
    
    @direccion.setter
    def direccion(self, valor):
        self._direccion = valor
        
    @property
    def telefono(self):
        return self._telefono
    
    @telefono.setter
    def telefono(self, value):
        self._telefono = value
        
    def verificarContrasena(self, contrasena):
        return self.__contrasena == contrasena
    
    def cambiarContrasena(self, nueva_contrasena):
        self.__contrasena= nueva_contrasena
        
    def obtenerRol(self):
        return "Usuario"
    
    def mostrarInformacion(self):
        print(f"Documento: {self._documento} | Nombre: {self._nombre} | "
            f"Email: {self._email} | Fecha de nacimiento: {self._fechaNacimiento} | "
            f"Dirección: {self._direccion} | Teléfono: {self._telefono} | "
            f"Rol: {self.obtenerRol()}")