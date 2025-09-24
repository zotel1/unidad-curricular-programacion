def multiplicacion():
    """
    Esta función pide al usuario que ingrese un numero a, 
    despues pide que ingrese un numero b y los multimplica
    """
    numero_a = int(input("Ingrese el numero a: "))
    numero_b = int(input("Ingrese el numero b: "))
    return numero_a * numero_b

def division():
    """
    Esta función pide al usuario que ingrese un numero a, 
    despues pide que ingrese un numero b y los y divide a entre b
    """
    numero_a = int(input("Ingrese el numero a: "))
    numero_b = int(input("Ingrese el numero b: "))
    return numero_a / numero_b


def suma():
    """
    Esta función pide al usuario que ingrese un numero a
    y despues un numero b y suma a con b
    """
    numero_a = int(input("Ingrese el numero a: "))
    numero_b = int(input("Ingrese el numero b: "))
    return numero_a + numero_b

def resta():
    """
    Esta función pide al usuario que ingrese un numero a
    y despues un numero b y resta a con b
    """
    numero_a = int(input("Ingrese el numero a: "))
    numero_b = int(input("Ingrese el numero b: "))
    return numero_a - numero_b

opcion = [1,2,3,4]

print("Elija una opción:") 
print("---------------------------------")
print("1 - Suma")
print("2 - Resta")
print("3 - Multiplicación")
print("4 - División")
print("0 - Salir!")
opcion = int(input("Elija una opción: "))

while(opcion != 0):
    
    if(opcion == 1):
        print("¡Elejiste sumar!")
        print(f"el resultado de tu suma es: {suma()}")
        
    elif(opcion == 2):
        print("¡Elejiste restar!")
        print(f"el resultado de tu resta es: {resta()}")
    elif(opcion == 3):
        print("¡Elejiste multiplicar!")
        print(f"el resultado de tu multiplicación es: {multiplicacion()}")
    elif(opcion == 4):
        print("¡Elejiste division!")
        print(f"el resultado de tu multiplicación es: {division()}")

    print("---------------------------------")

    print("Elija una opción:") 
    print("---------------------------------")
    print("1 - Suma")
    print("2 - Resta")
    print("3 - Multiplicación")
    print("4 - División")
    print("0 - Salir!")
    
    opcion = int(input("Elija una opción: "))

    

# def main():

   # print(f"La multiplicacion es: {multiplicacion()}")
#if __name__ == '__main__':
 #   main()