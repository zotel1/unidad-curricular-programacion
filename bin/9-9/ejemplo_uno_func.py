# 1-Escribir una funcion que muestre por pantalla el saludo "hola mundo" 
# cada vez que se llame a esa funcion.
# 2- escribir una funcion a la que se le pase una cadena 
# con el nombre que ingrese el usuario y muestre por pantalla un saludo personalizado
#
# escribir una funcion que calcule el total de una factura tras aplicarle el iva
#la funcion debe recibir la cantidad sin iva y el porcentaje de iva a aplicar
# y devolver el total de la factura

#

print("-----------------------------------")
print("Primer ejercicio: ")

n1 = int(input("Ingrese un numero: "))

def cuadrado(n1):
    
    return n1** 2

print(cuadrado(n1))

print("-----------------------------------")
print("Segundo ejercicio: ")

saludo = "Hola mundo"

def saludos(saludo):
    return saludo
print(saludos(saludo))

print("-----------------------------------")
print("Tercer ejercicio: ")

usuario = str(input("Ingrese su nombre: "))

def saludo_personalizado(usuario):
    return usuario
print("Buen inicio de semana, ",saludo_personalizado(usuario))












