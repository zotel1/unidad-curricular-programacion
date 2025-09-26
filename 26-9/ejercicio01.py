menu = ("Menu del cine")
print(menu)


entrada_cine = str(input("Quiere entrar a ver una pelicula?: [s/n]"))
while(entrada_cine == "s"):
    def control_acceso()->str:
        edad_espectador = int(input("Ingrese su edad: "))
        entrada_vip = str(input("Tiene entrada vip? [s/n]: "))
        if(edad_espectador != int('inf')):
            if(edad_espectador < 12):
                print("Acceso restringido.")
            elif(edad_espectador > 12 and edad_espectador < 17):
                print("Puede entrar solo con acompañante.")
            elif(edad_espectador > 17 and entrada_vip == "s"):
                print("Acceso total.")
            elif(edad_espectador > 17 and entrada_vip == "n"):
                    print("Acceso general.")
        return f"Para el usuario de {edad_espectador} años"
entrada_cine = str(input("Quiere entrar a ver una pelicula?: [s/n]"))



# def main():

    






#main()