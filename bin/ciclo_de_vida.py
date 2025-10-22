# Consigna:
#Un kiosco necesita un programa sencillo para registrar ventas de golosinas. 
# El programa debe:
#•Preguntar el nombre del producto.
#•Preguntar la cantidad.
#•Preguntar el precio unitario.
#•Calcular el total a pagar.


usuario = "s"
total_compra= 0
while(usuario == "s"):
    
    usuario = str(input("Desea comprar un producto? s/n: "))
    if(usuario == "s"):
        producto = str(input("Ingrese el nombre del producto: "))
        cantidad = int(input("Ingrese la cantidad de productos que desea: "))
        precio = float(input("Ingrese el precio unitario del producto: "))
        total = cantidad * precio
        
        print(f"El total de {cantidad} unidades de {producto}, es de {total} pesos.")
        total_compra += total
        print("-----------------------------------------")
    else:
        print(f"Muchas gracias, su total es: {total_compra} pesos, vuelva pronto.")
    