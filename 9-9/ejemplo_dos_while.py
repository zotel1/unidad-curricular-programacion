# escribir una funcion que calcule el total de una factura tras aplicarle el iva
#la funcion debe recibir la cantidad sin iva y el porcentaje de iva a aplicar
# y devolver el total de la factura

usuario = "s"
total_compra = 0
total_sin_iva = 0
precio = 0

while(usuario == "s"):
    
    print("-----------------------------------")
    print("¡Bienvenido al menu de factura de productos!")
    
    usuario = str(input("Desea comprar un producto? s/n:"))
    if(usuario == "s"):
        producto = str(input("Ingrese el producto a consultar: "))
        precio = int(input("Ingrese el precio del producto: "))
        iva = (precio * 21)
        
        def precio_iva(precio, iva):
            return iva / precio
        
        precio_total = precio_iva(precio, iva) + precio
        
        print(f"El producto seleccionado: {producto}, originalmente tiene el precio de: {precio}")
        print(f" su iva es de: {precio_iva(precio, iva)},") 
        print(f" y en total tendriamos que pagar {precio_total} pesos.")
        total_compra += precio_total
        total_sin_iva += precio
    elif(precio >= 1):
        print(f"Muchas gracias su total con iva es de {total_compra}")
        print(f"Su total sin iva es de: {total_sin_iva}")
    else:
        print("¡Muchas gracias, vuelva pronto!")