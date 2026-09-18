from sistema_vm import Sistema
from usuario import Usuario

sistema = Sistema()

opcion = 0

while opcion != 3:
    print("\n==========================")
    print("     VISION MADERA")
    print("\n==========================")
    print("1. Iniciar Sesión")
    print("2. Registrarse")
    print("3. Salir")
    print("\n==========================")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":

        email = input("Ingrese su email: ")
        contrasena = input("Ingrese su contraseña: ")

        usuario = sistema.iniciarSesion(email, contrasena)

        if usuario != None:

            print("Inicio de sesion exitoso!")
            usuario.mostrarInformacion()

            opcionUsuario = "0"

            while opcionUsuario != "3":

                print("\n==========================")
                print("      MENÚ DEL USUARIO")
                print("==========================")
                print("1. Agendar Cita")
                print("2. Ver mis citas")
                print("3. Cerrar Sesión")
                print("==========================")

                opcionUsuario = input("Seleccione una opcion: ")

                if opcionUsuario == "1":

                    print("\n===== AGENDAR CITA =====")

                    sistema.mostrarSedes()

                    idSede = input(
                        "\nSeleccione el punto de venta: "
                    )

                    sede = sistema.buscarSede(idSede)

                    if sede != None:

                        sistema.mostrarDisenadores(sede)

                        idDisenador = input(
                            "\nSeleccione el diseñador: "
                        )

                        disenador = sistema.buscarDisenador(
                            sede,
                            idDisenador
                        )

                        if disenador != None:

                            fecha = input(
                                "\nIngrese la fecha de la cita (AAAA-MM-DD): "
                            )

                            cita = sistema.agendarCita(
                                usuario,
                                sede,
                                disenador,
                                fecha
                            )

                            print("\n¡Cita agendada correctamente!")

                            cita.mostrarInformacion()

                        else:
                            print("\nEl diseñador seleccionado no existe.")

                    else:
                        print("\nLa sede seleccionada no existe.")

                elif opcionUsuario == "2":

                    print("\nEsta opción estará disponible próximamente.")

                elif opcionUsuario == "3":

                    print("\nSesión cerrada.")

                else:
                    print("\nOpcion inválida.")

        else:
            print("Email o contraseña incorrectos")

    elif opcion == "2":

        documento = input("Ingrese su documento: ")
        nombre = input("Ingrese su nombre: ")
        email = input("Ingrese su email: ")
        contrasena = input("Ingrese su contraseña: ")
        confirmarContrasena = input("Confirme su contraseña: ")
        fechaNacimiento = input("Ingrese su fecha de nacimiento: ")
        direccion = input("Ingrese su dirección: ")
        telefono = input("Ingrese su telefono/ celular: ")

        if contrasena == confirmarContrasena:

            usuario = Usuario(
                documento,
                nombre,
                email,
                contrasena,
                fechaNacimiento,
                direccion,
                telefono
            )

            if sistema.registrarUsuario(usuario):
                print("Usuario registrado correctamente!")
            else:
                print("El documento o email ya se encuentran registrados")

        else:
            print("Las contraseñas no coinciden")

    elif opcion == "3":

        print("Gracias por usar Vision Madera")

    else:

        print("Opcion inválida")