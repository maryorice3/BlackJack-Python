import random

def generar_carta():
    valor = random.randint(1, 13)
    if valor in [1, 11, 12, 13]:
        return 10
    return valor

def calcular_puntaje(mano):
    if 1 in mano and sum(mano) + 10 <= 21:
        return sum(mano) + 10
    return sum(mano)

def jugar_ganarle_al_croupier():
    print("¡Bienvenido al juego 'Ganarle al Croupier'!")

    # Generar una carta para cada jugador
    jugador = [generar_carta()]
    croupier = [generar_carta()]

    # Mostrar las cartas iniciales
    print("Carta del jugador:", jugador)
    print("Carta del croupier:", croupier[0])

    # Turno del jugador
    while True:
        accion = input("¿Deseas pedir otra carta (p) o plantarte (pl)? ")
        if accion.lower() == "p":
            jugador.append(generar_carta())
            print("Carta del jugador:", jugador)
            if calcular_puntaje(jugador) > 21:
                print("¡Te has pasado de 21! Has perdido.")
                return False
        elif accion.lower() == "pl":
            break

    # Turno del croupier
    while calcular_puntaje(croupier) <= 16:
        croupier.append(generar_carta())

    # Mostrar las cartas finales
    print("Carta del jugador:", jugador)
    print("Carta del croupier:", croupier)

    puntaje_jugador = calcular_puntaje(jugador)
    puntaje_croupier = calcular_puntaje(croupier)

    # Determinar el ganador
    if puntaje_jugador > 21:
        print("¡Te has pasado de 21! Has perdido.")
    elif puntaje_croupier > 21:
        print("El croupier se ha pasado de 21. ¡Has ganado!")
    elif puntaje_jugador > puntaje_croupier:
        print("¡Has ganado!")
    elif puntaje_jugador < puntaje_croupier:
        print("Has perdido.")
    else:
        print("¡Hay un empate!")

    return True

# Jugar varias rondas hasta que el jugador decida salir
while True:
    jugar = input("¿Deseas jugar una ronda de 'Ganarle al Croupier'? (s/n) ")
    if jugar.lower() == "s":
        print()
        if not jugar_ganarle_al_croupier():
            break
        print()
    else:
        break