#from random import randint
import random
lista =["piedra", "papel", "tijera"]
#usuario = "s"
contador_humano_total = 0
contador_robot_total = 0
#humano = ""
piedra = "piedra"
papel = "papel"
tijera = "tijera"


usuario = str(input("¿Queres jugar?: s/n "))
while (usuario == "s"):
    humano = str(input("¿Que elegis? ¿Piedra? ¿Papel? o ¿Tijera?: "))
    robot = random.choice(lista)
    
    print(f"El Robot eligio {robot}")

    
    
    
    def quien_gana():
        contador_humano = 0
        contador_robot = 0
        
    # def quien_gana(contador_humano, contador_robot):
        if(humano != ""):    
            if(humano == robot):
                print("¡Empate!")
            elif (humano == piedra and robot == papel):
                contador_humano = contador_humano + 1
                print("¡Gana humano!")
            elif(humano == papel and robot == piedra):
                contador_humano = contador_humano + 1
                print("¡Gana humano!")
            elif( humano == tijera and robot == papel):
                contador_humano = contador_humano + 1
                print("¡Gana humano!")
            else:
                contador_robot = contador_robot + 1
                print("¡Gana Robot!")
        else:
            print("Por favor elija uno")

        return (contador_humano, contador_robot)
    
    #h = quien_gana[0]
    #r = quien_gana[1]
    h, r = quien_gana()
    
    contador_humano_total += h
    contador_robot_total += r
    
    print(f"¡WAUU! El humano suma {contador_humano_total} mientras el Robot lleva {contador_robot_total} punto más!")
    
    usuario = str(input("¿Queres jugar?: s/n "))
    if (usuario == "n"):
        print(f"Juego terminado usted hizo {contador_humano_total} puntos y el robot hizo: {contador_robot_total} puntos")
        
    else:
        print(f"¡Fin del juego!")