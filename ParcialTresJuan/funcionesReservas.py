import time
reservar = []
reservarPorDestino = {
    "Torres del paine" : [],
    "Carretera Austral" : [],
    "Chiloé" : []
}
def registrarReserva(reservar,reservaDestino,nombre,apellido,origen,destino,cantidad):
    if destino in reservaDestino:
        reservaP = {
            "Nombre" : nombre,
            "Apellido" : apellido,
            "Ciudad Origen" : origen,
            "Destino" : destino,
            "Cantidad de personas": cantidad
        }
        reservar.append(reservaP)
        reservaDestino[destino].append(reservaP)
    else:
        print("El destino ingresado no se encuetra en la base de datos.")    
def verListaPersonas(reservas):
    if len(reservas) == 0:
        print("No se encontraron datos para mostrar, la lista esta vacía")   
    else:    
        for clave, valor in enumerate(reservas,start=1):
            nombre = valor["Nombre"]
            apellido = valor["Apellido"]
            origen = valor["Ciudad Origen"]
            destino = valor["Destino"]
            cantidadP = valor["Cantidad de personas"]
            print(f"Cliente: {nombre} { apellido} Ciudad Origen: {origen} Tour: {destino} Cantidad Personas: {cantidadP} ")
def imprimirLista(reservasDestino,destino):
    if destino in reservasDestino:
        try:
            print("Estamos generando su lista de reservas, Favor esperar...")
            print("3...")
            time.sleep(1)
            print("2...")
            time.sleep(1)
            print("1...")
            time.sleep(1)
            with open(f"detallesVenta_{destino}.txt","w",encoding="utf-8") as archivo:
                archivo.write("Cliente\tCiudad Origen\tTour\tCantidad Personas\n")
                for clave, valor in enumerate(reservarPorDestino[destino],start=1):
                    nombre = valor["Nombre"]
                    apellido = valor["Apellido"]
                    origen = valor["Ciudad Origen"]
                    destinoU = valor["Destino"]
                    cantidadP = valor["Cantidad de personas"]
                    archivo.write(f"Nombre: {nombre.capitalize()} {apellido.capitalize()}\tCiudad Origen: {origen.capitalize()}\t Tour: {destinoU}\t Cantidad{cantidadP}\n")
            print("El documento se genero con exito, Verlo en la barra izquierda del programa.")
        except ValueError:
            print("Algo a ocurrido al imprimir sus reservas, Favor verificar.")        
    else:
        print("El destino ingresado no se encuentra en la base de datos")        
