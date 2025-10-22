menu = ("------------------Menu del cine------------------")
print(menu)
entrada_cine = str(input("Quiere entrar a ver una pelicula?: [s/n]"))

while(entrada_cine == "s"):
    if(entrada_cine == "s"):
        edad_usuario_total = 0
        while True:
            try:
                numero = int(input("Ingrese un número entero: "))
                
                edad_usuario_total += numero
                break
            except ValueError:
                print("Error: Debe ingresar un número entero. Inténtelo de nuevo.")   
        entrada_vip = str(input("Tiene entrada vip? [s/n]: "))
        while(True):
            edad = 0
            edad += edad_usuario_total
            
            if(edad < 12):
                print("Disculpe, tiene usted ¡Acceso restringido!.")
                break
            elif(edad > 12 and edad < 17):
                print("Usted puede entrar solo con acompañante.")
                break
            elif(edad > 17 and entrada_vip == "s"):
                print("Muy bien, tiene usted ¡Acceso total!")
                break
            elif(edad > 17 and entrada_vip == "n"):
                print("Muy bien, tiene usted ¡Acceso general!")
                break   
    else:
        print("Solo se acepta el ingreso de las teclas: [s/n]")
    print(menu)
    entrada_cine = str(input("Quiere entrar a ver una pelicula?: [s/n]"))
    
print("Gracias por su visita, vuelva pronto.")