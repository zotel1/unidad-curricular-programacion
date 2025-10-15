import random

"""
Conclusion del trabajo, el metodo shuflle, 
reorganiza d emanera aleatoria el diccionario, 
despues el usuario puede elegir entre uno de los 
primeros 3 elementos de la nueva lista reorganizada, 
y la maquina elige uno de los 3 siguientes elementos de la lista
"""
"""
# Baraja española (solo números, sin 8 ni 9)
palos = ["Espada", "Basto", "Oro", "Copa"]
numeros = [1,2,3,4,5,6,7,10,11,12]

# Jerarquía simplificada del Truco argentino
jerarquia = {
    (1, "Espada ⚔️"): 14,
    (1, "Basto 🪵"): 13,
    (7, "Espada ⚔️"): 12,
    (7, "Oro 🪙"): 11,
    (3, None): 10,
    (2, None): 9,
    (1, "Copa 🍷"): 8,
    (12, None): 7,
    (11, None): 6,
    (10, None): 5,
    (7, None): 4,
    (6, None): 3,
    (5, None): 2,
    (4, None): 1
}

#Contadores
puntos_usuario_total = 0
puntos_cpu_total = 0
cantidad_de_manos = 0

juego = str(input("Queres jugar al truco?: [s/n] "))
while(juego == "s"):
    while(puntos_usuario_total or puntos_cpu_total != 15):
        def fuerza(carta):
            num, palo = carta
            # Reglas especiales
            if (num, palo) in jerarquia:
                return jerarquia[(num, palo)]
            elif (num, None) in jerarquia:
                return jerarquia[(num, None)]
            else:
                return 0
            
        #print(f"LA carta mas alta es {fuerza((1,'Espada'))}")

        def crear_mazo():
            return [(n, p) for n in numeros for p in palos]
        #print("creamos el mazo",crear_mazo())


        def mostrar_mano(mano):
            for i, (n,p) in enumerate(mano, 1):
                print(f"{i}. {n} de {p}")
            return mano

        def carta_manos():
            
            carta = random.choice(list(jerarquia.keys()))
            numero, palo = carta

            if palo is None:
                primera = f"Primera carta [{numero}]"
            else:
                primera = f"Primera carta [{numero} de {palo}]"
            return primera

            
            mazo = crear_mazo()
            carta_uno = random.choice(mazo)
            carta_dos = random.choice(mazo)
            carta_tres = random.choice(mazo)
            
            resultado = {carta_uno[0]: carta_uno[1], carta_dos[0]: carta_dos[1],carta_tres[0]: carta_tres[1]}
            #primera = f"Primera carta [{resultado[0]} de {resultado[1]}]"
            return resultado
        
        def crear_mano()->list:
            
            #random.shuffle(mazo)

            mano_jugador = carta_manos()
            #mano_jugador = random.choice(mazo[:15])
            mano_cpu = carta_manos()
            print("La cpu saco",mano_cpu)

            print("Tus cartas son: ", mano_jugador)
        
            carta_cpu = random.choices(mano_cpu).__dict__
            #print(random.choices(carta_cpu))
            #print("La computadora jugó:", mano_cpu, "de", mano_cpu)
            print(f"La computadora eligio {carta_cpu}")
            #carta_jugador = mano_jugador
            #carta_cpu = mano_cpu


            eleccion = int(input("Elige una carta (1-3): ")) - 1
            carta_jugador = mano_jugador[eleccion].__dict__
            print("Jugaste:", carta_jugador[0], "de", carta_jugador[1])

            
                # CPU juega aleatoria
            #carta_cpu = random.choice(mano_cpu)
            #print("La computadora jugó:", carta_cpu[0], "de", carta_cpu[1])
            return [carta_cpu, carta_jugador]

        print(crear_mano())


        def jugar():
            print()
            carta_cpu = crear_mano().index(0)
            carta_jugador = crear_mano().index(1)
            
            puntos_usuario = 0
            puntos_cpu = 0
                #mazo = crear_mazo()
                #random.shuffle(mazo)
                #mazo = crear_mano()

                #mano_jugador = mazo[:3]
                #mano_cpu = mazo[3:6]

                #print("Tus cartas son:")
                #mostrar_mano(mano_jugador)

                # jugador elige carta
                #eleccion = int(input("Elige una carta (1-3): ")) - 1
                #carta_jugador = mano_jugador[eleccion]
                #print("Jugaste:", carta_jugador[0], "de", carta_jugador[1])

                # CPU juega aleatoria
                #carta_cpu = random.choice(mano_cpu)
                #print("La computadora jugó:", carta_cpu[0], "de", carta_cpu[1])
            #CPU juega aleatoria
            #todas_las_cartas = [carta for palo in mano_cpu for carta in palo]

            

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
        
        puntos_usuario, puntos_cpu = jugar()
        puntos_usuario_total += puntos_usuario
        puntos_cpu_total += puntos_cpu

            #jugar ()

# def main():
  #  juego = str(input("Queres jugar al truco?: [s/n] "))
   # while(juego == "s"):
    #    while(puntos_usuario_total or puntos_cpu_total != 15):
     #       fuerza()
      #      jugar()


#main()


"""


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

def manos_cartas():
    mazo = crear_mazo()
    carta_uno = random.choices(mazo)
    mazo.pop(random.randint(0, len(mazo) - 1))
    #mazo.remove(carta_uno)
    carta_dos = random.choices(mazo)
    #mazo.remove(carta_dos)
    mazo.pop(random.randint(0, len(mazo) - 1))
    carta_tres = random.choices(mazo)
    #mazo.remove(carta_tres)
    mazo.pop(random.randint(0, len(mazo) - 1))
    mano_jugador = carta_uno, carta_dos, carta_tres
    carta_uno = random.choices(mazo)
    mazo.pop(random.randint(0, len(mazo) - 1))
    #mazo.remove(carta_uno)
    carta_dos = random.choices(mazo)
    #mazo.remove(carta_dos)
    mazo.pop(random.randint(0, len(mazo) - 1))
    carta_tres = random.choices(mazo)
    #mazo.remove(carta_tres)
    mazo.pop(random.randint(0, len(mazo) - 1))
    mano_cpu = carta_uno, carta_dos, carta_tres

    print(mazo)
    return mano_jugador, mano_cpu

mano_jugador, mano_cpu = manos_cartas()
#print("Mano humano sin descomprimir",mano_jugador)
#print("Mano cpu sin decomprimir",mano_cpu)
lista_tuplas_jug = [tupla for lista in mano_jugador for tupla in lista]
lista_tuplas_cpu = [tupla for lista in mano_cpu for tupla in lista]
#print(lista_tuplas_jug)
#print(lista_tuplas_cpu)

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
    mano_cpu.pop(random.randint(0, len(mano_cpu) - 1))

    # jugador elige carta
    eleccion = int(input("Elige una carta (1-3): ")) - 1
    carta_jugador = mano_jugador[eleccion]
    print("Jugaste:", carta_jugador[0], "de", carta_jugador[1])
    mano_jugador.pop(random.randint(0, len(mano_cpu) - 1))


    return (carta_jugador, carta_cpu)

def jugar():

    puntos_usuario = 0
    puntos_cpu = 0

    

    carta_jugador, carta_cpu = manos()
    
    while(carta_jugador != 0 and carta_cpu != 0 ):
        # Comparar fuerza
        if fuerza(carta_jugador) > fuerza(carta_cpu):
            puntos_usuario += 1 
            print("¡Ganaste la baza! ")
            
        elif fuerza(carta_jugador) < fuerza(carta_cpu):
            puntos_cpu += 1
            print("La computadora ganó la baza ")
            
        else:
            print("Empate ")
        break

    return (puntos_usuario, puntos_cpu)

puntos_usuario, puntos_cpu = jugar()
puntos_usuario_total += puntos_usuario
puntos_cpu_total += puntos_cpu

#jugar()

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
    main()