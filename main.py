from sistema_vm import Sistema
from usuario import Usuario
#Modulo principal (Main) del sistema donde se gestiona por medio de consola el flujo de la aplicacion
#Presenta el menú principal y el menú de usuarios de forma interactiva para agendar, consultar, editar y cancelar citas.

sistema = Sistema()
opcion = "0"

def fechaValida(fechaTexto):
    partes= fechaTexto.split("-")
    if len(partes)!=3:
        return False
    anio, mes, dia= partes
    if not (anio.isdigit() and mes.isdigit() and dia.isdigit()):
        return False
    if len(anio)!=4 or len(mes)!=2 or len(dia) != 2:
        return False
    if int(mes) <1 or int(mes) > 12:
        return False
    if int(dia) <1 or int(dia) > 31:
        return False
    return True
#Valida si el string de fecha ingresado cumple con AAAA-MM-DD y sus valores son coherentes

while opcion != "3":
#Bucle principal de la aplicacion: Menu de bienvenida con opciones para inicio de aplicacion , registro y salida del sistema.
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
            
            while opcionUsuario != "5":
            #Bucle secundario de sesion de usuario ya autenticado la cual permite interactuar con las opciones de agendamiento,
            #Viasualizacion, Edicion, Cancelacion de citas y el cierre de la sesion del usuario actual.
                print("\n==========================")
                print("      MENÚ DEL USUARIO")
                print("==========================")
                print("1. Agendar Cita")
                print("2. Ver mis citas")
                print("3. Editar cita")
                print("4. Cancelar cita")
                print("5. Cerrar Sesión")
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
                            fecha = input("\nIngrese la fecha de la cita (AAAA-MM-DD): ")
                            while not fechaValida(fecha):
                                print("La fecha debe tener el formato AAAA-MM-DD (Ejemplo: 2005-03-21)")
                                fecha= input("\nIngrese la fecha de la cita (AAAA-MM-DD): ")
                            sistema.mostrarBloquesHorarios()
                            idBloque= input(
                                "\nSeleccione el horario: "
                            )
                            bloqueHorario= sistema.buscarBloqueHorario(idBloque)
                            if bloqueHorario != None:
                                cita = sistema.agendarCita(
                                    usuario,
                                    sede,
                                    disenador,
                                    fecha,
                                    bloqueHorario
                                )
                                if cita != None:
                                    print("\nCita agendada correctamente!")
                                    cita.mostrarInformacion()
                                else:
                                    print("\nEse diseñador ya tiene una cita asignada en ese horario.")
                            else:
                                print("\nEl horario seleccionado no existe.")
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
                    sistema.mostrarSedes()
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
                    fecha = input(f"Fecha (AAAA-MM-DD) [{cita.fecha}]: ")
                    while fecha != "" and not fechaValida(fecha):
                        print("La fecha debe tener el formato AAAA-MM-DD (Ejemplo: 2005-03-21)")
                        fecha= input(f"Fecha (AAAA-MM-DD) [{cita.fecha}]: ")
                    fecha = fecha if fecha != "" else cita.fecha
                    sistema.mostrarBloquesHorarios()
                    idBloque= input(
                        f"Horario [{cita.bloqueHorario.horaInicio} - "
                        f"{cita.bloqueHorario.horaFin}]: "
                    )
                    bloqueHorario= (
                        sistema.buscarBloqueHorario(idBloque)
                        if idBloque != ""
                        else cita.bloqueHorario
                    )
                    if bloqueHorario is None:
                        print("\nEl horario seleccionado no esxiste.")
                        continue
                    if sistema.modificarMisCitas(
                        usuario,
                        numeroCita,
                        sede,
                        disenador,
                        fecha,
                        bloqueHorario
                    ):
                        print("\n¡Cita modificada correctamente!")
                        citasUsuario[numeroCita - 1].mostrarInformacion()
                        
                    else:
                        print("\nNo fue posible modificar la cita.")
                        
                elif opcionUsuario == "4":
                    citasUsuario = sistema.obtenerMisCitas(usuario)
                    if len(citasUsuario) == 0:
                        print("\nNo tienes citas agendadas.")
                        continue
                    print("\n===== CANCELAR CITA =====")
                    for numeroCita, cita in enumerate(citasUsuario, start=1):
                        print(
                            f"{numeroCita}. {cita.sede.nombre} - "
                            f"{cita.disenador.nombre} - {cita.fecha}"
                        )
                    numeroCita = input("Seleccione la cita que desea cancelar: ")
                    if not numeroCita.isdigit():
                        print("\nLa cita seleccionada no es válida.")
                        continue
                    numeroCita = int(numeroCita)
                    if numeroCita < 1 or numeroCita > len(citasUsuario):
                        print("\nLa cita seleccionada no es válida.")
                        continue
                    if sistema.cancelarCita(usuario, numeroCita):
                        print("\n¡Cita cancelada correctamente!")
                    else:
                        print("\nNo fue posible cancelar la cita.")
                        
                elif opcionUsuario == "5":
                    print("\nSesión cerrada.")
                    
                else:
                    print("\nOpcion inválida.")
        else:
            print("Email o contraseña incorrectos")
            
    elif opcion == "2":
        documento = input("Ingrese su documento: ")
        nombre = input("Ingrese su nombre: ")
        email = input("Ingrese su email: ")
        while "@" not in email or "." not in email:
            print("El correo debe contener @ y un dominio (Ejemplo: nombre@dominio.com)")
            email= input("Ingrese su email: ")
        contrasena = input("Ingrese su contraseña: ")
        confirmarContrasena = input("Confirme su contraseña: ")
        while contrasena != confirmarContrasena:
            print("Las contraseñas no coinciden. Intente de nuevo.")
            contrasena = input("Ingrese su contraseña: ")
            confirmarContrasena = input("Confirme su contraseña: ")
        fechaNacimiento = input("Ingrese su fecha de nacimiento (AAAA-MM-DD): ")
        while not fechaValida(fechaNacimiento):
            print("La fecha debe tener el formato AAAA-MM-DD (Ejemplo: 2005-03-21)")
            fechaNacimiento= input("Ingrese su fecha de nacimiento (AAAA-MM-DD): ")
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
                
    elif opcion == "3":
        print("Gracias por usar Vision Madera")
    else:
        print("Opcion inválida")