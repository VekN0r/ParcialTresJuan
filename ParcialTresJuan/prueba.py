from funcionesReservas import *
while True:
    print(f"*"*30)
    print("1.-Registrar reservas: ")
    print("2.-Ver Listado de reservas: ")
    print("3.-Imprimir detalles por destino: ")
    print("4.-Salir") 
    print(f"*"*30)
    opc = input("Ingrese una opción a realizar: ")
    if opc == "1":
        try:
            print("===Bienvenido al Sistema de reservas===")
            nombre = input("Ingrese nombre: ").lower()
            apellido = input("Ingrese apellido: ").lower()
            origen = input("Ingrese la ciudad de origen: ").lower()
            destino = input("Ingrese lugar de destino: ")
            cantidadP = input("Ingrese la cantidad de boletos: ").lower()
            if len(nombre) == 0 or len(apellido) == 0 or len(origen) == 0 or len(destino) == 0 or len(cantidadP) == 0:
                print("Uno de los datos ingresados no contiene ningun caracter, Favor de ingresarlos correctamente")
            else:
                registrarReserva(reservar,reservarPorDestino,nombre,apellido,origen,destino,cantidadP)
        except ValueError:
            print("Hubo un error al registrar la reserva")
    elif opc == "2":
        verListaPersonas(reservar)
    elif opc == "3":
        destino = input("Ingrese que destino desea imprimir. Torres del Paine, Carretera Austral y/o Chiloé") 
        imprimirLista(reservarPorDestino,destino) 
    elif opc == "4":
        print("Saliendo del programa...")
        time.sleep(1)
        print("Hasta la proxima")
        break     
    else:
        print("Opción fuera de rango")             

