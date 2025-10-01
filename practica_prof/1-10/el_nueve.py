import random

# Crear baraja española de 40 (sin 8 y 9)
def crear_baraja():
    palos = ["Oro", "Copa", "Espada", "Basto"]
    valores = {
        1: 11, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7,
        10: 10, 11: 10, 12: 10
    }
    baraja = []
    for palo in palos:
        for numero in valores:
            baraja.append((numero, palo, valores[numero]))
    random.shuffle(baraja)
    return baraja

# Calcular valor de la mano
def valor_mano(mano):
    total = sum(carta[2] for carta in mano)
    ases = sum(1 for carta in mano if carta[0] == 1)
    while total > 21 and ases:
        total -= 10
        ases -= 1
    return total

# Mostrar cartas
def mostrar_mano(nombre, mano):
    cartas = ", ".join([f"{c[0]} de {c[1]}" for c in mano])
    print(f"{nombre}: {cartas} (Total: {valor_mano(mano)})")

# Juego principal
def blackjack_espanol():
    baraja = crear_baraja()
    jugador = [baraja.pop(), baraja.pop()]
    banca = [baraja.pop(), baraja.pop()]

    print("=== Blackjack con cartas españolas ===")
    mostrar_mano("Tus cartas", jugador)
    print(f"Carta visible de la banca: {banca[0][0]} de {banca[0][1]}")

    # Turno del jugador
    while valor_mano(jugador) < 21:
        accion = input("¿Querés otra carta (p) o plantarte (s)? ").lower()
        if accion == "p":
            jugador.append(baraja.pop())
            mostrar_mano("Tus cartas", jugador)
        else:
            break

    if valor_mano(jugador) > 21:
        print("Te pasaste de 21. Pierdes ")
        return

    # Turno de la banca
    print("\nTurno de la banca...")
    mostrar_mano("Banca", banca)
    while valor_mano(banca) < 17:
        banca.append(baraja.pop())
        mostrar_mano("Banca", banca)

    # Resultado
    total_jugador = valor_mano(jugador)
    total_banca = valor_mano(banca)

    print("\n=== RESULTADO FINAL ===")
    mostrar_mano("Tus cartas", jugador)
    mostrar_mano("Banca", banca)

    if total_banca > 21 or total_jugador > total_banca:
        print("¡Ganaste! ")
    elif total_jugador == total_banca:
        print("Empate ")
    else:
        print("Gana la banca ")

# Ejecutar
blackjack_espanol()
