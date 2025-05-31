
def move_to_front(lista_numeros, solicitudes):
    costo_total = 0
    for elemento in solicitudes:
        print(f"Solicitud: {elemento}") #Imprimir el elemento que estamos solicitando
        print(f"Estado inicial de la configuración: {lista_numeros}")
        print(f"Costo inicial: {costo_total}")
        posicion_item = lista_numeros.index(elemento) #Buscar el elemento deseado
        numero_a_mover = lista_numeros.pop(posicion_item) #Eliminar 
        lista_numeros.insert(0, numero_a_mover)
        print(f"Lista luego de mover al frente la solictud: {lista_numeros}")
        costo_total += posicion_item +1
        print(f"Costo luego de la solicitud: {costo_total}")
        print("--------")

    return costo_total

def i_move_to_front(lista_numeros, solicitudes):
    costo_total = 0
    for elemento in solicitudes:
        print(f"Solicitud: {elemento}") #Imprimir el elemento que estamos solicitando
        print(f"Estado inicial de la configuración: {lista_numeros}")
        print(f"Costo inicial: {costo_total}")
        posicion_item = lista_numeros.index(elemento) + 1 #Buscar el elemento deseado, sumamos 1 ya que para este algoritmo asumimos que la primera posición es i=1
        pos_inicial = solicitudes.index(elemento) +1  #Guardamos la posición inicial en la lista de solicitudes
        limit = posicion_item -1
        print("Limit: ", limit)
        if limit > len(solicitudes):
            look_ahead = solicitudes[pos_inicial:] # verificamos si está dentro de los límites
        else:
            look_ahead = solicitudes[pos_inicial:(pos_inicial+ limit)] #Buscar en las próxima
        print(f"Look_ahead: {look_ahead}")
        if elemento in look_ahead: #Verificar si está en look ahead
            numero_a_mover = lista_numeros.pop(posicion_item -1) #Eliminar 
            lista_numeros.insert(0, numero_a_mover) #Mover al frente
            print(f"Lista luego de mover al frente la solictud: {lista_numeros}")
        costo_total += posicion_item
        print(f"Costo luego de la solicitud: {costo_total}")
        print("--------")

    return costo_total
            
    

condicion = True
while condicion:
    print("-------------------------------")
    print("Bienvenido, seleccione su opción")


    print("Caso 1: Configuración [0,1,2,3,4], solicitudes: [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]")
    print("Caso 2: Configuración: [0,1,2,3,4], solictudes: [4, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4] ")
    print("Caso 3: Mejor caso con 20 solicitudes, configuración: [0,1,2,3,4], solicitudes: [0]*20")
    print("Caso 4: Peor caso con 20 solicitudes, configuración: [0,1,2,3,4], solcititudes: [4,3,2,1,0] * 4 ")
    print("Caso 5: Configuración: [0,1,2,3,4], solicitudes: [2]*20")
    print("Caso 6: Configuración: [0,1,2,3,4], solicitudes: [3]*20")

    opcion = int(input("Opción: "))

    algoritmo = int(input("Seleccione el algoritmo: 1. MTF    2. IMTF  "))

    if opcion == 1:
        if algoritmo == 1:
            print(f"Costo total: {move_to_front([0,1,2,3,4], [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4])}")
        else: 
            print(f"Costo total: {i_move_to_front([0,1,2,3,4], [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4])}")
    elif opcion == 2:
        if algoritmo == 1:
            print(f"Costo total: {move_to_front([0,1,2,3,4], [4, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4])}")
        else: 
            print(f"Costo total: {i_move_to_front([0,1,2,3,4], [4, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4])}")
    elif opcion == 3:
        if algoritmo == 1:
            print(f"Costo total: {move_to_front([0,1,2,3,4], [0]*20)}")
        else: 
            print(f"Costo total: {i_move_to_front([0,1,2,3,4], [0]*20)}")
    elif opcion == 4:
        if algoritmo == 1:
            print(f"Costo total: {move_to_front([0,1,2,3,4], [4,3,2,1,0]*4)}")
        else: 
            print(f"Costo total: {i_move_to_front([0,1,2,3,4], [4,3,2,1,0]*4)}")
    elif opcion == 5:
        if algoritmo == 1:
            print(f"Costo total: {move_to_front([0,1,2,3,4], [2]*20)}")
        else: 
            print(f"Costo total: {i_move_to_front([0,1,2,3,4], [2]*20)}")
    elif opcion == 6:
        if algoritmo == 1:
            print(f"Costo total: {move_to_front([0,1,2,3,4], [3]*20)}")
        else: 
            print(f"Costo total: {move_to_front([0,1,2,3,4], [3]*20)}")
    

