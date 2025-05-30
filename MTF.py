
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

    return costo_total
            
    




