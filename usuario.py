class Usuario:
    #Representa a un usuario registrado dentro del sistema
    
    def __init__(self, documento, nombre, email, contrasena, fechaNacimiento, direccion, telefono):
        self._documento=documento
        self.nombre=nombre
        self.email=email
        self.__contrasena=contrasena
        self.fechaNacimiento=fechaNacimiento
        self.direccion=direccion
        self.telefono=telefono
    #Instancia de la clase usuario
        
    @property
    def documento(self):
        return self._documento
    #Obtiene el documento de identidad
    
    @property
    def nombre(self):
        return self._nombre
    #Obtiene o establece el nombre del usuario
    
    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor
        
    @property
    def email(self):
        return self._email
    #Obtiene o establece el correo electrónico del usuario
    
    @email.setter
    def email(self, valor):
        self._email = valor
        
    @property
    def fechaNacimiento(self):
        return self._fechaNacimiento
    #Obtiene o establece la fecha de nacimiento del usuario
    
    @fechaNacimiento.setter
    def fechaNacimiento(self, valor):
        self._fechaNacimiento = valor
        
    @property
    def direccion(self):
        return self._direccion
    #Obtiene o establece la dirección de residencia del usuario
    
    @direccion.setter
    def direccion(self, valor):
        self._direccion = valor
        
    @property
    def telefono(self):
        return self._telefono
    #Obtiene o establece el teléfono de contacto del usuario
    
    @telefono.setter
    def telefono(self, value):
        self._telefono = value
        
    def verificarContrasena(self, contrasena):
        return self.__contrasena == contrasena
    #Verifica si la contraseña ingresada coincide con la contraseña almacenada
    
    def cambiarContrasena(self, nueva_contrasena):
        self.__contrasena= nueva_contrasena
    #Actualiza la contraseña del usuario.
        
    def obtenerRol(self):
        return "Usuario"
    #Obtiene el rol correspondeinte el usuario en el sistema (Por defecto Usuario)
    
    def mostrarInformacion(self):
        print(f"Documento: {self._documento} | Nombre: {self._nombre} | "
            f"Email: {self._email} | Fecha de nacimiento: {self._fechaNacimiento} | "
            f"Dirección: {self._direccion} | Teléfono: {self._telefono} | "
            f"Rol: {self.obtenerRol()}")
    #Imprime en consola todos los datos generales del usuario y su rol