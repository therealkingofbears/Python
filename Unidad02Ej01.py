#FUNCION
def es_mayor(numeros):
    mayor = numeros[0]
    count = 1
    
    for numero in numeros:
        if numero > mayor:
            mayor = numero
            count = 1
        elif numero == mayor:
            count += 1
        
    if count > 1:
        print("-1")
        return -1
    else:
        print("Mayor:", mayor)
        return mayor

    
    

#PRINCIPAL
numeros = []
for i in range(3):
    numero = int(input("Ingrese un número entero " .format(i + 1)))
    numeros.append(numero)

es_mayor(numeros)