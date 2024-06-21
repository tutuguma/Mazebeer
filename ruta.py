
# El algoritmo toma como calculo principal la distancia Manhattan
def distancia_taxi(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# El algoritmo toma como calculo principal la distancia Manhattan
def encontrar_ruta(mapa, inicio, fin):
    filas = len(mapa)
    columnas = len(mapa[0])
    cola = [(0, inicio, [])] # Inicializamos la cola con costo 0, coordenada:inicio y la ruta vacia
    visitados = set() # Se usa para evitar que no se repitan coordenadas conjunto vacio pero no se puede usar asi visitados{} pq python piensa que es dict

    while cola:
        costo_total, (x, y), ruta = min(cola, key=lambda x: x[0]) #Funcion flecha que retorna la cola de costo min
        cola.remove((costo_total, (x, y), ruta))
        nodo = (x, y)

        if nodo == fin:  #Si la coordenada  llega al fin retornar la lista de las rutas con todos los pasos(nodos) que se dieron
            return ruta + [nodo]

        if nodo in visitados: #Si la coordenada ya paso por visitado entonces saltar
            continue

        visitados.add(nodo) #Agregar al conjunto inicial vacio la coordenada por donde se paso

        movimientos = [(0, 1), (0, -1), (1, 0), (-1, 0),(-1, 1),(-1, -1),(1, 1),(1, -1)] #Posibles movimientos, izq,der,arriba,abajo y las diagonales superiores e inferiores
        for dx, dy in movimientos:
            nueva_x, nueva_y = x + dx, y + dy 
            nuevo_nodo = (nueva_x, nueva_y) #nueva coordenada gracias al movimiento

            if (
                0 <= nueva_x < filas # se verifica que la nueva x este dentro del rango de filas la matriz
                and 0 <= nueva_y < columnas # se verifica que la nueva y este dentro del rango de filas la matriz
                and mapa[nueva_x][nueva_y] == 0 # se verifica que el valor del nuevo nodo es igual a 0
                and nuevo_nodo not in visitados # si el nuevo nodo no esta en visitados
            ):
                nueva_ruta = ruta + [nodo]
                nuevo_costo = len(nueva_ruta) + distancia_taxi(nuevo_nodo, fin)
                cola.append((nuevo_costo, nuevo_nodo, nueva_ruta))

    return [] 

    
def imprimir_mapa(mapa, ruta=None, inicio=None, fin=None):
    for fila in range(len(mapa)):
        for columna in range(len(mapa[0])):
            celda = mapa[fila][columna]
            if (fila, columna) == fin:
                print("🍺", end=" ")
           
            elif ruta and (fila, columna) in ruta:
                print("🧔", end=" ")
           
            elif celda == 0:
                print("⬜", end=" ")
            elif celda == 1:
                print("🚧", end=" ")  # Edificio
            elif celda == 2:
                print("🆓", end=" ")  # Agua
            elif celda == 3:
                print("🔥", end=" ")  # Fuego

            

            
        print()

def colocar_obstaculo(mapa):
    obstaculos = []
    while True:
        respuesta = input("¿Desea colocar un obstáculo? S/N: ")
        if respuesta.upper() == "S":
            while True:
                try:
                    tipo = int(input('''
                    Elija el tipo de bloqueo:
                    1: Edificios u obstáculos que no se pueden atravesar.
                    2: Agua u otros obstáculos que requieren una ruta alternativa.
                    3: Fuego o areas de incendio '''))
                    if 1 <= tipo <= 3:
                        break
                    else:
                        print("Opción inválida")
                except ValueError:
                    print("Ingrese un número válido para el tipo de obstáculo.")
            
            coordenada_obstaculo = ingresar_coordenadas("Ingrese las coordenadas del obstáculo", len(mapa), len(mapa[0]))
            
            if mapa[coordenada_obstaculo[0]][coordenada_obstaculo[1]] == 0:
                mapa[coordenada_obstaculo[0]][coordenada_obstaculo[1]] = tipo
                obstaculos.append(coordenada_obstaculo)
                print(f"Obstáculo tipo {tipo} colocado en {coordenada_obstaculo}")
            else:
                print("Ya hay un obstáculo en esa posición.")
        
        elif respuesta.upper() == "N":
            break
        else:
            print("Debe responder con 'S' o 'N'")
    return obstaculos

def ingresar_coordenadas(mensaje, filas, columnas):
    while True:
        try:
            fila = int(input(f"{mensaje} (fila): "))
            columna = int(input(f"{mensaje} (columna): "))

            if 0 <= fila < filas and 0 <= columna < columnas:
                return fila, columna
            else:
                print("Coordenadas fuera del rango del mapa.")
        except ValueError:
            print("Por favor, ingrese números enteros válidos.")

mapa = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

print("Mapa inicial:")
imprimir_mapa(mapa)

obstaculos_agregados = colocar_obstaculo(mapa)
print("\nMapa con obstáculos agregados:")
imprimir_mapa(mapa)

inicio = ingresar_coordenadas("Ingrese las coordenadas de inicio", len(mapa), len(mapa[0]))
fin = ingresar_coordenadas("Ingrese las coordenadas de fin", len(mapa), len(mapa[0]))

ruta = encontrar_ruta(mapa, inicio, fin)

if ruta:
    print("\nRuta encontrada:")
    imprimir_mapa(mapa, ruta,inicio,fin)
else:
    print("No se encontró una ruta.")