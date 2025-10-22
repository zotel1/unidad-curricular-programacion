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

def mostrar_mano(mano):
            for i, (n,p) in enumerate(mano, 1):
                print(f"{i}. {n} de {p}")
            return mano
print("mostramos la mano",mostrar_mano([(1,"Espada"),(3,"Copa"),(12,"Oro")]))
            
def crear_mazo():
        return [(n, p) for n in numeros for p in palos]

print("creamos el mazo",crear_mazo())


def crear_mano():
            mazo = crear_mazo()
            random.shuffle(mazo)

            mano_jugador = random.choice(mazo[:15])
            mano_cpu = random.choice(mazo[15:30])
            print("La cpu saco",mano_cpu)

            print("Tus cartas son:")
            mostrar_mano(mano_jugador)