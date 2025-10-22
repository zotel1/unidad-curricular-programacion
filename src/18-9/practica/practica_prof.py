ingrese_valor = int(input("Ingrese un valor: "))


print(f"El usuario ingreso el numero {ingrese_valor}")

if(ingrese_valor == 0):
    print("Ingrese un valor diferente de 0")
elif(ingrese_valor % 2):
    print(f"El numero {ingrese_valor} no par")
else:
    print(f"El numero {ingrese_valor} es par")

ingrese_palabra = str(input("Ingrese una palabra: "))
contar_letras = len(ingrese_palabra)
print(f"La palabra ingresada por el usuario {ingrese_palabra} tiene {contar_letras} letras")

edad_usuario = int(input("Ingrese su edad: "))
cuantos_falta = 50 - edad_usuario
anio_actual = 2025
cuando_cumple_cincuenta = anio_actual + cuantos_falta
print(f"La edad del usuario es de: {edad_usuario} y faltan {cuantos_falta} años para que cumpla 50 años")
print(f"El usuario va a cumplir 50 años en el año {cuando_cumple_cincuenta}")
