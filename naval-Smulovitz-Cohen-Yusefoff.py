# Variables constantes
N = 10
CANTIDAD_BARCOS = 10
DISPAROS = 15

# Crear tableros vacíos
tablero1 = [[0 for _ in range(N)] for _ in range(N)]
tablero2 = [[0 for _ in range(N)] for _ in range(N)]

posiciones_ocupadas1 = set()
posiciones_ocupadas2 = set()

# Ingresa el jugador 1 las posiciones de los barcos
while len(posiciones_ocupadas1) < CANTIDAD_BARCOS:
    fila1 = int(input(f"Jugador 1: Ingrese la fila (0 a {N-1}) en donde quiere colocar su barco: "))
    columna1 = int(input(f"Jugador 1: Ingrese la columna (0 a {N-1}): en donde quiere colocar su barco: "))
    if (fila1, columna1) in posiciones_ocupadas1:
         print("Ya hay un barco ahí. Ingrese una coordenada válida.")
         continue

    if (fila1 < 0 or fila1 >= N or columna1 < 0 or columna1 >= N):
                print("Su barco está fuera del tablero. Ingrese una coordenada válida.")
                continue

    if (fila1, columna1) not in posiciones_ocupadas1:
        posiciones_ocupadas1.add((fila1, columna1))
        tablero1[fila1][columna1] = 1

# Jugador 2
while len(posiciones_ocupadas2) < CANTIDAD_BARCOS:
    fila2 = int(input(f"Jugador 2: Ingrese la fila (0 a {N-1}) en donde quiere colocar su barco: "))
    columna2 = int(input(f"Jugador 2: Ingrese la columna (0 a {N-1}) en donde quiere colocar su barco: "))
    if (fila2, columna2) in posiciones_ocupadas2:
         print("Ya hay un barco ahí. Ingrese una coordenada válida.")
         continue

    if (fila2 < 0 or fila2 >= N or columna2 < 0 or columna2 >= N):
                print("Su barco está fuera del tablero. Ingrese una coordenada válida.")
                continue

    if (fila2, columna2) not in posiciones_ocupadas2:
        posiciones_ocupadas2.add((fila2, columna2))
        tablero2[fila2][columna2] = 1

# Variables de disparos del jugador
aciertos = 0
fallos = 0
disparos_realizados = set()
aciertos2 = 0
fallos2 = 0
disparos_realizados2 = set()

for turno in range(DISPAROS): 
    print(f"\nDisparo {turno + 1} de {DISPAROS}")
    
    # El jugador ingresa las coordenadas a donde disparar 
    print("Turno del jugador 1")   
    while True:
        try:
            fila2 = int(input(f"Ingresa la fila (0 a {N-1}): "))
            columna2 = int(input(f"Ingresa la columna (0 a {N-1}): "))
            if (fila2, columna2) in disparos_realizados:
                print("Ya disparaste ahí. Probá otra coordenada.")
            elif 0 <= fila2 < N and 0 <= columna2 < N:
                break
            else:
                print("Coordenadas fuera del tablero. Probá de nuevo.")
        except ValueError:
            print("Solo se pueden números enteros")

    disparos_realizados.add((fila2, columna2))

    # Si acertó:
    if tablero2[fila2][columna2] == 1:
        print("Hundido")
        tablero2[fila2][columna2] = "X"  
        aciertos += 1

    # Si no acertó:
    else:
        print("Agua")
        tablero2[fila2][columna2] = "-"  
        fallos += 1

        print("Turno del jugador 2")   
    
    # Jugador 2
    while True:
        try:
            fila1 = int(input(f"Ingresa la fila (0 a {N-1}): "))
            columna1 = int(input(f"Ingresa la columna (0 a {N-1}): "))
            if (fila1, columna1) in disparos_realizados2:
                print("Ya disparaste ahí. Probá otra coordenada.")
            elif 0 <= fila1 < N and 0 <= columna1 < N:
                break
            else:
                print("Coordenadas fuera del tablero. Probá de nuevo.")
        except ValueError:
            print("Solo se pueden números enteros")

    disparos_realizados2.add((fila1, columna1))

    if tablero1[fila1][columna1] == 1:
        print("Hundido")
        tablero1[fila1][columna1] = "X"  
        aciertos2 += 1

    else:
        print("Agua")
        tablero1[fila1][columna1] = "-"  
        fallos2 += 1

# Mostrar resultados
print("Fin del juego! Resultados:")
print("Jugador 1:")
print(f"Aciertos: {aciertos}")
print(f"Fallos: {fallos}\n")


# Mostrar tablero final
print("Tablero final:")
for fila1 in tablero1:
    print(" ".join(str(x) for x in fila1))

# Jugador 2
print("Jugador 2:")
print(f"Aciertos: {aciertos2}")
print(f"Fallos: {fallos2}\n")

print("Tablero final:")
for fila2 in tablero2:
    print(" ".join(str(x) for x in fila2))