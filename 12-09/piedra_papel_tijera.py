#from random import randint
import random
lista =["piedra", "papel", "tijera"]
humano = str(input("¿Que elegis? ¿Piedra? ¿Papel? o ¿Tijera?: "))
robot = random.choice(lista)
piedra = "piedra"
papel = "papel"
tijera = "tijera"
print(f"La computadora eligio {robot}")

if (humano== tijera and robot == papel):
    print("Gana humano")
elif (humano == papel and robot == piedra):
    print("Gana humano")
elif (humano == piedra and robot == tijera):
    print("Gana humano")
else:
    print("Empate")


