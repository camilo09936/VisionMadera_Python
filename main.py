from sistema_vm import Sistema
from usuario import Usuario

sistema= Sistema()

opcion= 0
while opcion != 3:
    print("\n==========================")
    print("     VISION MADERA")
    print("\n==========================")
    print("1. Iniciar Sesión")
    print("2. Registrarse")
    print("3. Salir")
    print("\n==========================")
    
    opcion= int(input("Seleccione una opcion: "))
    
    if opcion == 1:
        email= input("Ingrese su email: ")
        contrasena= input("Ingrese su contraseña: ")
        
        usuario= sistema.iniciarSesion(email,contrasena)
        
        if usuario != None:
            print("Inicio de sesion exitoso!")
            usuario.mostrarInformacion()
        else:
            print("Email o contraseña incorrectos")
            
    elif opcion == 2:
        documento= input("Ingrese su documento: ")
        nombre= input("Ingrese su nombre: ")
        email= input("Ingrese su email: ")
        contrasena= input("Ingrese su contraseña: ")
        confirmarContrasena= input("Confirme su contraseña: ")
        fechaNacimiento= input("Ingrese su fecha de nacimiento: ")
        direccion= input("Ingrese su dirección: ")
        telefono= input("Ingrese su telefono/ celular: ")
        
        if contrasena == confirmarContrasena:
            usuario= Usuario(documento, nombre, email, contrasena, fechaNacimiento, direccion, telefono)
            if sistema.registrarUsuario(usuario):
                print("Usuario registrado correctamente!")
            else:
                print("El documento o email ya se encuentran registrados")
        else:
            print("Las contraseñas no coinciden")
        
    elif opcion == 3:
        print("Gracias por usar Vision Madera")
    else:
        print("Opcion inválida")