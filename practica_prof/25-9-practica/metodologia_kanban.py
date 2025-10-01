productos = ["-Pan", "-Arroz", "-Azúcar", "-Aceite"
"-Fideos"
"-Harina Común",
"-Harina Leudante",
"-Levadura"
"-Queso Cremoso"
"-Salsa Lista"]

precios = [1600,1400,
1000,
2900,
1000,
900,
1500,
800,
2000,
1800]

def mostrar():
    for i in range (len (productos)):
        print (f"{i+1}, {productos} {[i]}, {precios[i]}" )

mostrar()

"""
Esta función debe poder calcular el valor total de todos los productos 
que el usuario decide llevarse.
Para realizar esta tarea debemos crear una variable que cumplirá la función de contador, 
por lo cual al iniciar la función calcular el total, 
esta variable debe tener el valor de cero.
Dentro de una estructura repetitiva se debe poder mostrar la lista de productos disponibles 
y una variable donde se almacenara las decisiones del usuario. 
(Se puede usar la estructura while True:).
Mediante una estructura repetitiva If podemos hacer las comparaciones entre 
lo que pide el usuario y los productos que tenemos disponible.
Para evitar que se convierta en un bucle infinito 
debemos de poder pornerle una opcion de salida, o una palabra clave. 
Ejemplo if opcion == "fin": //opción es una variable donde se almacena la decision del usuario
break //break es una palabra clave que lo saca del bucle while True

en una siguiente estructura if debemos asegurarnos que 
los datos ingresados por el usuario sean numeros para eso podemos utilizar la siguiente metodo.
if opcion.isdigit(): //esta condición permitirá ejecutar las instrucciones 
que escribamos dentro de la
//estructura if solo si la opción ingresada por el usuario es un digito

indice = int(opcion) - 1 //volvemos a declarar una variable llamada indice y le restamos 1 a la opcion
//ingresada por el usuario, debido que las listas en python empiezan en el 0 y las
//opciones que le damos al usuario empiezan por uno.
Debemos crear mesajes de error en el caso de que el usuario no ingrese un numero y otro en el caso que el usuario ingrese un numero mayor a 10 (El total de productos que poseemos en nuestras listas es 10)
"""

