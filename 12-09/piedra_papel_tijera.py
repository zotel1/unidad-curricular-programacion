#from random import randint
import random
lista =["piedra", "papel", "tijera"]
#usuario = "s"
contador_h_total = 0
contador_r_total = 0
#humano = ""
piedra = "piedra"
papel = "papel"
tijera = "tijera"
contador_humano = 0
contador_robot = 0
contador_humano_suma = 0
contador_robot_suma = 0


usuario = str(input("¿Queres jugar?: s/n "))
while (usuario == "s"):
    humano = str(input("¿Que elegis? ¿Piedra? ¿Papel? o ¿Tijera?: "))
    robot = random.choice(lista)
    contador_humano = 0
    contador_robot = 0
    print(f"El Robot eligio {robot}")
    
    puntos = 0
    def quien_gana(puntos):
        
    #def quien_gana(contador_humano, contador_robot):
        if(humano != ""):
            if(humano == robot):
                print("¡Empate!")
            elif (humano == piedra and robot == papel):
                contador_humano += 1
                print("¡Gana humano!")
            elif(humano == papel and robot == piedra):
                contador_humano += 1
                print("¡Gana humano!")
            elif( humano == tijera and robot == papel):
                contador_humano += 1
                print("¡Gana humano!")
            #elif (robot == piedra and humano == papel):
            #    contador_robot += 1
             #   print(f"¡Gana el Robot y suma {contador_robot} punto!")
            #elif(robot == papel and humano == piedra):
             #   contador_robot += 1
              #  print(f"¡Gana el Robot y suma {contador_robot} punto!")
            #elif(robot == tijera and humano == papel):
             #   contador_robot += 1
              #  print(f"¡Gana el Robot y suma {contador_robot} punto!")
            else:
                contador_robot += 1
                print("¡Gana Robot!")
            puntos += (contador_robot or contador_humano)
        else:
            print("Por favor elija uno")

            
        
        return puntos
    contador_humano += contador_humano_suma
    contador_robot += contador_robot
    print(f"¡WAUU! Suma {quien_gana(puntos)} punto más!")
        
    #print("Aca anted sel elif")
  #  contador_h_total += quien_gana(contador_humano , contador_robot)
   # contador_r_total += quien_gana(contador_robot, contador_humano)
    usuario = str(input("¿Queres jugar?: s/n "))
    if (usuario == "n"):
        #print("Durante")
        print(f"Juego terminado usted hizo {contador_h_total} puntos y el robot hizo: {contador_r_total} puntos")
        
    else:
        print(f"¡Fin del juego!")
    
#print("Fin del juego")