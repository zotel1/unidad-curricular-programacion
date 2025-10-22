# Escribir un programa que lea un entero positivo, n, introducido por el usuario y 
# luego muestre en pantalla la suma de todos los enteros desde 1 hasta n.
# la suma de los n primeros enteros positivos puede ser calculada con la fórmula: suma = n(n + 1) / 2

def suma_enteros(n, m):
    return n * (n + m) / 2
n = int(input('Ingrese un numero entero positivo: '))
m = 1

print(f'La suma de los {n} primeros enteros positivos es: {suma_enteros(n, m)}')

