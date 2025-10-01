import random

# Baraja española (solo números, sin 8 ni 9)
palos = ["Espada", "Basto", "Oro", "Copa"]
numeros = [1,2,3,4,5,6,7,10,11,12]

# Jerarquía simplificada del Truco argentino
jerarquia = {
    (1, "Espada"): 14,
    (1, "Basto"): 13,
    (7, "Espada"): 12,
    (7, "Oro"): 11,
    (3, None): 10,
    (2, None): 9,
    (1, None): 8,
    (12, None): 7,
    (11, None): 6,
    (10, None): 5,
    (7, None): 4,
    (6, None): 3,
    (5, None): 2,
    (4, None): 1
}

def fuerza(carta):
    num, palo = carta
    # Reglas especiales
    if (num, palo) in jerarquia:
        return jerarquia[(num, palo)]
    elif (num, None) in jerarquia:
        return jerarquia[(num, None)]
    else:
        return 0

def crear_mazo():
    return [(n, p) for n in numeros for p in palos]

def mostrar_mano(mano):
    for i, (n,p) in enumerate(mano, 1):
        print(f"{i}. {n} de {p}")

#Contadores
puntos_usuario_total = 0
puntos_cpu_total = 0
cantidad_de_manos = 0


# def crear_mano():
 #   for i in range(0,cantidad_de_manos):
  #      mazo = crear_mazo()
   #     random.shuffle(mazo)


def jugar():
    puntos_usuario = 0
    puntos_cpu = 0
    mazo = crear_mazo()
    random.shuffle(mazo)
    #mazo = crear_mano()

    mano_jugador = mazo[:3]
    mano_cpu = mazo[3:6]

    print("Tus cartas son:")
    mostrar_mano(mano_jugador)

    # jugador elige carta
    eleccion = int(input("Elige una carta (1-3): ")) - 1
    carta_jugador = mano_jugador[eleccion]
    print("Jugaste:", carta_jugador[0], "de", carta_jugador[1])

    # CPU juega aleatoria
    carta_cpu = random.choice(mano_cpu)
    print("La computadora jugó:", carta_cpu[0], "de", carta_cpu[1])

    # Comparar fuerza
    if fuerza(carta_jugador) > fuerza(carta_cpu):
        puntos_usuario += 1 
        print("¡Ganaste la baza! ")
    elif fuerza(carta_jugador) < fuerza(carta_cpu):
        puntos_cpu += 1
        print("La computadora ganó la baza ")
    else:
        print("Empate ")
    return (puntos_usuario, puntos_cpu)

u, c = jugar()
puntos_usuario_total += u
puntos_cpu_total += c

#jugar ()

juego = str(input("Queres jugar al truco?: [s/n] "))

while(juego == "s"):
    while(puntos_usuario_total or puntos_cpu_total != 15):
        jugar()



