# escribir una funcion que calcule el total de una factura tras aplicarle el iva
#la funcion debe recibir la cantidad sin iva y el porcentaje de iva a aplicar
# y devolver el total de la factura
print("-----------------------------------")
print("¡Buen dia!")

print("Factura producto:")
producto = str(input("Ingrese el producto a consultar: "))
precio = int(input("Ingrese el precio del producto: "))

iva = (precio * 21)

def precio_iva(precio, iva):
    
    return iva / precio

print(f"El producto seleccionado: {producto}, originalmente tiene el precio de: {precio}, su iva es de: {precio_iva(precio, iva)}, y en total tendriamos que pagar {precio_iva(precio, iva) + precio} pesos.")