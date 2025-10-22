n1 = int(input("Ingrese el valor de a: "))
n2 = int(input("Ingrese el valor de b: "))
n3 = int(input("Ingrese el valor de c: "))

if(n1>n2):
    if(n1>n3):
        print(f"El numero mayor es el valor de a: {n1}")
        #print(f"El numero mayor es el valor de a: ", n1)
elif(n2>n3):
    print(f"El numero mayor es el valor de b: {n2}")
else:
    print(f"El numero mayor es el valor de c: {n3}")
if(n1 == n2):
    print(f"Hay dos numeros iguales, a: {n1} y b: {n2}" )
elif(n1 == n3):
    print(f"Hay dos numeros iguales, a: {n1} y c: {n3} ")
elif(n2 == n3):
    print(f"Hay dos numeros iguales, el valor de b: {n2} y el valor de c: {n3}")