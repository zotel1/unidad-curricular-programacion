"""
Pida al usuario que ingrese 2 números 
y luego muestre el resultado de sumarlos.
"""

numero_a = int(input("Ingrese el numero a: "))

numero_b = int(input("Ingrese el numero b: "))

def suma():
    """
    Esta función suma los numeros enteros a y b
    """
     
    
    return numero_a + numero_b

#mensaje = print(f"el resultado de la suma entre el numero a {numero_a} y el numero b {numero_b}, es: {total})

#mensaje = print(f"print(f"el resultado de la suma entre el numero a {numero_a} y el numero b {numero_b}, es: {total}")
def main():
    total = suma()
    print(f"el resultado de la suma entre el numero a:[{numero_a}] y el numero b:[{numero_b}], es:[{total}]")
    
if __name__== '__main__':
    main()