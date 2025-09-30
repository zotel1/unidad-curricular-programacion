menu = ("Menu del cine")
print(menu)
edad_usuario_total = 0

entrada_cine = str(input("Quiere entrar a ver una pelicula?: [s/n]"))

while(entrada_cine == "s"):
    edad_entero = int(input("Ingrese su edad: "))
    if (edad_entero == ""):
        print("¡Por favor ingresa un numero entero!")
    else:
        
        edad_usuario_total += edad_entero
        print(f"Edad prueba {edad_usuario_total}")
        break
    
          

#entrada_cine = str(input("Quiere entrar a ver una pelicula?: [s/n]"))
if(entrada_cine == "s"):
    while(entrada_cine == "s"):
        edad += edad_usuario
        edad = (input("Ingrese su edad: "))
        entrada_vip = str(input("Tiene entrada vip? [s/n]: "))
        if(edad < 12):
            print("Acceso restringido.")
        elif(edad > 12 and edad < 17):
            print("Puede entrar solo con acompañante.")
        elif(edad > 17 and entrada_vip == "s"):
            print("Acceso total.")
        elif(edad > 17 and entrada_vip == "n"):
            print("Acceso general.")
        #else:
        #    print("Por favor ingrese un numero entero.")
        
    entrada_cine = str(input("Quiere entrar a ver una pelicula?: [s/n]"))
else:
    print("Solo se acepta el ingreso de las teclas: [s/n]")



# def main():

    






#main()