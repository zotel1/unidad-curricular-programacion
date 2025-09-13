import math

"""
para calcular el volumen de un cilindro V=π⋅r⋅r⋅h
"""

print("----------------------------")
radio = int(input("Ingrese el radio para calcular el Area de un círculo: "))
def calcular_area(radio):
    res_radio = radio * radio
    return res_radio * (math.pi)

print(calcular_area(radio))

