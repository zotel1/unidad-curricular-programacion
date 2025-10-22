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
    (3, "Espada"): 10, 
    (3, "Basto"): 310, 
    (3, "Oro"): 10, 
    (3, "Copa"): 10,
    (2, "Espada"): 9, 
    (2, "Basto"): 9, 
    (2, "Oro"): 9, 
    (2, "Copa"): 9,
    (1, "Oro"): 8,
    (1, "Copa"): 8,
    (12,"Espada"): 7,
    (12,"Basto"): 7,
    (12,"Oro"): 7,
    (12,"Copa"): 7,
    (11,"Espada"): 6,
    (11,"Basto"): 6,
    (11,"Oro"): 6,
    (11,"Copa"): 6,
    (10,"Espada"): 5,
    (10,"Basto"): 5,
    (10,"Oro"): 5,
    (10,"Copa"): 5,
    (7, "Basto"): 4,
    (7, "Copa"): 4,
    (6,"Espada"): 3,
    (6,"Basto"): 3,
    (6,"Oro",): 3,
    (6,"Copa"): 3,
    (5,"Espada"): 2,
    (5,"Basto"): 2,
    (5,"Oro"): 2,
    (5,"Copa"): 2,
    (4,"Espada"): 1,
    (4,"Basto"): 1,
    (4,"Oro"): 1,
    (4,"Copa"): 1
}


#Contadores
puntos_usuario_total = 0
puntos_cpu_total = 0
cantidad_de_manos = 0

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

"""
def manos_cartas():
    mazo = crear_mazo()
    random.shuffle(mazo) # MEzclamos el mazo aleatoriamente

    #mazo_lista: list[list[int, str]] = [list(tupla) for tupla in mazo]

    print(f"MAZO: {mazo}")
    print("CARTAS JUGADOR:")

    carta_uno_jug = random.choices(mazo)
    #print(carta_uno_jug)
    #indice_carta_uno_jug = mazo.index(carta_uno_jug)
    #mazo.pop(indice_carta_uno_jug)
    
    
    #mano_jugador += carta_uno_jug
    # Ejemplo: eliminar sublistas que cumplan una condición
    
    mazo = [sub for sub in mazo if sub != carta_uno_jug]   

    carta_dos_jug = random.choices(mazo)
    #indice_carta_dos_jug = mazo.index(carta_dos_jug)
    #mazo.pop(indice_carta_dos_jug)

    mazo = [sub for sub in mazo if sub != carta_dos_jug]   

    

    

    carta_tres_jug = random.choice(mazo)
    #indice_carta_tres_jug = mazo.index(carta_tres_jug)
    #mazo.pop(indice_carta_tres_jug)
    mazo = [sub for sub in mazo if sub != carta_tres_jug]   
    

    mano_jugador = [carta_uno_jug, carta_dos_jug, carta_tres_jug]
    print(f"ESTAS SON LAS CARTAS DEL JUGADOR{mano_jugador}")
    

    carta_uno_cpu = random.choice(mazo)
    
    #indice_carta_uno_cpu = mazo.index(carta_uno_cpu)
    #mazo.pop(indice_carta_uno_cpu)
    #print(carta_uno_cpu)

    #mazo = mazo

    mazo = [sub for sub in mazo if sub != carta_uno_cpu]   

    carta_dos_cpu = random.choices(mazo)
    

    #indice_carta_dos_cpu = mazo.index(carta_dos_cpu)
    #mazo.pop(indice_carta_dos_cpu)

    mazo = [sub for sub in mazo if sub != carta_dos_cpu] 
    
    carta_tres_cpu = random.choices(mazo)
    mazo = [sub for sub in mazo if sub != carta_tres_cpu] 
    #indice_carta_tres_cpu = mazo.index(carta_tres_cpu)
    #mazo.pop(indice_carta_tres_cpu)
    
    #mazo = mazo
    mano_cpu = carta_uno_cpu, carta_dos_cpu, carta_tres_cpu
    print(f"ESTAS SON LAS CARTAS DE LA CPU[{mano_cpu}]")
    print(f"MAZO SIN LAS 6 CARTAS{mazo}")
    return mano_jugador, mano_cpu
print(manos_cartas())


mano_jugador, mano_cpu = manos_cartas()

lista_tuplas_jug = [tupla for lista in mano_jugador for tupla in lista]
lista_tuplas_cpu = [tupla for lista in mano_cpu for tupla in lista]


def manos():
    
    mano_jugador = lista_tuplas_jug
    mano_cpu = lista_tuplas_cpu

    print("A la computadora le tocaron las siguientes cartas: ")
    mostrar_mano(mano_cpu)
    print("A vos te tocaron las siguientes cartas: ")
    mostrar_mano(mano_jugador)


    # CPU juega aleatoria
    carta_cpu = random.choice(mano_cpu)
    print("La computadora jugó:", carta_cpu[0], "de", carta_cpu[1])
    #mano_cpu.pop(random.randint(0, len(mano_cpu) - 1))
    indice_carta_cpu = mano_cpu.index(carta_cpu)
    mano_cpu.pop(indice_carta_cpu)
    #mano_cpu.pop(carta_cpu)

    # jugador elige carta
    eleccion = int(input("Elige una carta (1-3): ")) - 1
    carta_jugador = mano_jugador[eleccion]
    print("Jugaste:", carta_jugador[0], "de", carta_jugador[1])
    #mano_jugador.pop(random.randint(0, len(mano_jugador) - 1))
    indice_carta_jug = mano_jugador.index(carta_jugador)
    mano_jugador.pop(indice_carta_jug)
    #mano_jugador.pop(carta_jugador)


    return [carta_jugador, carta_cpu]
"""

def manos_cartas():
    mazo = crear_mazo()

    #repartimos 3 cartas al jugador
    mano_jugador = [mazo.pop() for _ in range(3)]

    # repartimos 3 cartas a la cpu
    mano_cpu = [mazo.pop() for _ in range(3)]

    print("Cartas del jugador:")
    mostrar_mano(mano_jugador)
    print("\nCartas de la CPU:")
    mostrar_mano(mano_cpu)

    print(f"\nMazo restante ({len(mazo)} cartas): {mazo}")


    return mano_jugador, mano_cpu
def jugar():

    puntos_usuario = 0
    puntos_cpu = 0

    

    carta_jugador, carta_cpu = manos_cartas()
    
    while(carta_jugador and carta_cpu ):
        # Comparar fuerza
        if fuerza(carta_jugador) > fuerza(carta_cpu):
            puntos_usuario += 1 
            print(f"¡Ganaste la mano! Tu {carta_jugador} es mayor que el {carta_cpu} de la computadora")
            
        elif fuerza(carta_jugador) < fuerza(carta_cpu):
            puntos_cpu += 1
            print(f"¡La computadora ganó la mano! Su {carta_cpu} es mayor que tu {carta_jugador}")
            
        else:
            print("Empate ")
    
        #break

    return (puntos_usuario, puntos_cpu)

puntos_usuario, puntos_cpu = jugar()
puntos_usuario_total += puntos_usuario
puntos_cpu_total += puntos_cpu

print("Vas sumando: ", puntos_usuario_total)
print("La computadora va sumando: ", puntos_cpu_total)

jugar()

"""

def main():
    queres_jugar = str(input("Queres jugar al truco? [s/n]: "))
    while(queres_jugar == "s"):
        cuantos_puntos = int(input("¿Cuantos puntos por mano? [15 o 30]: "))
        if(cuantos_puntos < 16):
            while(puntos_usuario_total or puntos_cpu_total < 16):
                jugar()
        elif(cuantos_puntos < 31):
            while(puntos_usuario_total or puntos_cpu_total < 31):
                jugar()






if __name__ == '__main__':
    main()"""