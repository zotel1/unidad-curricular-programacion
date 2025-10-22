# Importamos a la biblioteca random
import random

#Lista con opciones
lista =["piedra", "papel", "tijera"]

#Contadores finales
contador_humano_total = 0
contador_robot_total = 0

#Definimos las variables para despues compararlas, en formato string
piedra = "piedra"
papel = "papel"
tijera = "tijera"

#El usuario decide si quiere jugar y lo guardamos en la variable inicio_juego en tipo de dato string
inicio_juego = str(input("¿Queres jugar?: s/n "))
#Pedimos al usuario que ingrese su nombre y lo guardamos en la variable usuario en tipo de dato string
usuario = str(input("¿Como te llamas?: "))

#Iniciamos el juego con un ciclo while siempre que el usuario haya escrito s
while (inicio_juego == "s"):
    #Pedimos al usuario que elija entre piedra papel o tijera y lo almacenamos en la variable humano, tipo de dato string
    humano = str(input("¿Que elegis? ¿Piedra? ¿Papel? o ¿Tijera?: "))

    #Utilizamos el metodo choice para que elija de la lista uno de los valores de la misma de manera aleatoria
    robot = random.choice(lista)
    
    #Imprimimos lo que eligio el robot
    print(f"El Robot eligio {robot}")
    
    # Creamos nuestra funcion para comparar los resultados y comenzar el juego
    def quien_gana():
        #Comenzamos con nuestros contadores en cero
        contador_humano = 0
        contador_robot = 0
        
    # iniciamos el juego si el humano en este caso eligio un valor diferente a un string vacio
    #ademas el valor que eligio el humano no debe ser diferente a piedra, papel o tijera
        if(humano != "" and humano ==piedra or humano == papel or humano == tijera):
            # Hacemos la comparacion, si ambos son iguales obtenemos un empate    
            if(humano == robot):
                print("¡Empate!")
            #Comparamos si el humano tiene piedra y el robot tijeta, sumamos 1 punto al contador_humano
            elif (humano == piedra and robot == tijera):
                contador_humano = contador_humano + 1
            #Si el nombre del usuario es diferente a un string vacio, imprimimos el mensaje con su nombre
                if(usuario !=""):
                    print(f"¡Gana {usuario}!")
            #Si el usuario no ingreso un nombre, solo imprimimos el mensaje
                else:
                    print("¡Ganaste!")
            #Comparamos si el humano tiene papel y el robot piedra, sumamos 1 punto al contador_humano
            elif(humano == papel and robot == piedra):
                contador_humano = contador_humano + 1
            #Si el nombre del usuario es diferente a un string vacio, imprimimos el mensaje con su nombre
                if(usuario !=""):
                    print(f"¡Gana {usuario}!")
            #Si el usuario no ingreso un nombre, solo imprimimos el mensaje
                else:
                    print("¡Ganaste!")
            #Comparamos si el humano tiene tijera y el robot papel, sumamos 1 punto al contador_humano
            elif( humano == tijera and robot == papel):
                contador_humano = contador_humano + 1
            #Si el nombre del usuario es diferente a un string vacio, imprimimos el mensaje con su nombre
                if(usuario !=""):
                    print(f"¡Gana {usuario}!")
            #Si el usuario no ingreso un nombre, solo imprimimos el mensaje
                else:
                    print("¡Ganaste!")
            # Si no se cumple todo lo anterior, sumamos un punto al contador_robot
            else:
                contador_robot = contador_robot + 1
                print("¡Gana Robot!")
            #Este else es por si el usuario no elijio nada o si elijio una palabra diferente a piedra papel o tijera
        else:
            print("¡Si no elije una opcion no se puede jugar!")
            print("¡Por favor elija una opcion!")
            #Retornamos el valor de contador_humano, contador_robot
        return (contador_humano, contador_robot)
    
    #Al retornar los dos valores separados por coma, que estos no sean una lista, un diccionario o un string
    #Python nos retorna una tupla
    #desempaquetamos los valores de la tupla
    #En la letra h el valor de contador_humano
    #En la letra r el valor de contador_robot
    h, r = quien_gana()
    
    #Hacemos uso del contador_humano_total sumandole el valor de h
    contador_humano_total += h
    #Hacemos uso del contador_robot_total sumandole el valor de r
    contador_robot_total += r
    #Decimos que si contador_humano_total y contador_robot_total es menor que 1 nos responda que nadie suma puntos
    #Este if puede suceder cuando en la primera comparacion ambos elijen lo mismo
    if(contador_humano_total < 1 and contador_robot_total < 1):
        print("Nadie suma puntos!")
    #Si el alguno de los contadores es mayor a 1 nos imprime el siguiente mensaje, 
    # mostrandonos el valor de los contadores totales actualmente
    else:
        print(f"¡WAUU! Vos tenes {contador_humano_total} puntos y el Robot tiene {contador_robot_total} puntos!")
    # Volvemos a preguntar al usuario si quiere jugar
    #Si el usuario teclea s, volvemos  iniciar el ciclo
    inicio_juego = str(input("¿Queres jugar?: s/n "))
    #Si el usuario teclea n nos puede imprimir un mensale u otro
    if (inicio_juego == "n"):
    # Si la variable usuario es diferente a un string vacio nos imprime el siguiente mensaje
        if(usuario !=""):
            print(f"Puntaje final: {usuario} hizo {contador_humano_total} puntos y el robot hizo: {contador_robot_total} puntos")
    #Si el usuario no escribio un nombre y la variable usuario contiene un string vacio, imprime el siguiente mensaje
        else:
            print(f"Puntaje final: Al final hiciste {contador_humano_total} puntos y el robot hizo: {contador_robot_total} puntos")
    #Si el usuario teclea cualquier letra nos imprime este mensaje
    else:
        print(f"¡Fin del juego!")
#Al final del programa despedimos al usuario
print(f"¡Fin del juego gracias por participar {usuario}!")