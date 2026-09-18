from sistema_vm import Sistema
from usuario import Usuario

sistema = Sistema()

opcion = "0"

while opcion != "3":
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

            while opcionUsuario != "4":

                print("\n==========================")
                print("      MENÚ DEL USUARIO")
                print("==========================")
                print("1. Agendar Cita")
                print("2. Ver mis citas")
                print("3. Editar cita")
                print("4. Cerrar Sesión")
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

                    sistema.mostrarMisCitas(usuario)

                elif opcionUsuario == "3":

                    citasUsuario = sistema.obtenerMisCitas(usuario)

                    if len(citasUsuario) == 0:
                        print("\nNo tienes citas agendadas.")
                        continue

                    print("\n===== EDITAR CITA =====")
                    for numeroCita, cita in enumerate(citasUsuario, start=1):
                        print(
                            f"{numeroCita}. {cita.sede.nombre} - "
                            f"{cita.disenador.nombre} - {cita.fecha}"
                        )

                    numeroCita = input("Seleccione la cita que desea editar: ")

                    if not numeroCita.isdigit():
                        print("\nLa cita seleccionada no es válida.")
                        continue

                    numeroCita = int(numeroCita)

                    if numeroCita < 1 or numeroCita > len(citasUsuario):
                        print("\nLa cita seleccionada no es válida.")
                        continue

                    cita = citasUsuario[numeroCita - 1]
                    print("\nDeje un campo vacío para conservar su valor actual.")

                    idSede = input(
                        f"Sede [{cita.sede.nombre}]: "
                    )
                    sede = (
                        sistema.buscarSede(idSede)
                        if idSede != ""
                        else cita.sede
                    )

                    if sede is None:
                        print("\nLa sede seleccionada no existe.")
                        continue

                    sistema.mostrarDisenadores(sede)
                    idDisenador = input(
                        f"Diseñador [{cita.disenador.nombre}]: "
                    )
                    disenador = (
                        sistema.buscarDisenador(sede, idDisenador)
                        if idDisenador != ""
                        else cita.disenador
                    )

                    if disenador is None:
                        print("\nEl diseñador seleccionado no existe.")
                        continue

                    fecha = input(f"Fecha [{cita.fecha}]: ")
                    fecha = fecha if fecha != "" else cita.fecha

                    if sistema.modificarMisCitas(
                        usuario,
                        numeroCita,
                        sede,
                        disenador,
                        fecha
                    ):
                        print("\n¡Cita modificada correctamente!")
                        citasUsuario[numeroCita - 1].mostrarInformacion()
                    else:
                        print("\nNo fue posible modificar la cita.")

                elif opcionUsuario == "4":

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
        fechaNacimiento = input("Ingrese su fecha de nacimiento (AAAA-MM-DD): ")
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