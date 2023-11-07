# Definición de funciones

def es_multiplo(a,b):
    return a % b == 0

def cant_divisores(num):
    cant = 1
    for i in range(2,num+1):
        if es_multiplo(num, i):
            cant += 1
    return cant

def es_primo(num):
    return cant_divisores(num) == 2



# Programa principal
numero = int(input("Ingrese un número entero"))
print("El número ",end="") # Esto se usa para que no haya salto de línea

if not es_primo(numero):
    print("NO ",end="")
print("Es PRIMO")