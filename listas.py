#Listas son similares a los vectores: se crean asignando a una variable una secuencia de elementos encerrados entre corchetes[] y separados por comas. Se puede crear una lista vacía, y las listas pueden ser elementos de otras listas

numeros = [1,2,3,4,5] #lista de números
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"] #listas de caracteres
elementos = [] #lista vacía
matriz = [ [1,2,3], [4,5,6]] #lista dentro de listas, se configuran como matrices

print(dias[0]) #primera posición de la lista días, en este caso Lunes
suma = 0

for i in range(len(numeros)):
    suma = suma + numeros[i]
print(suma) #20

#for in

vocales = ["a", "e", "i", "o", "u"]
for i in vocales: #recorre la lista e imprime cada elemento de la lista en una línea vertical
    print(i)
    
#Desempaquetado

diass = ["Lunes", "Martes", "Miércoles"]
d1, d2, d3 = diass
print(d1)
print(d2)
print(d3)

#Concatenado
lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = lista1 + lista2

print(lista3)

#La función list() convierte cualquier secuencia en una lista
""" 
.pop() remueve una posición. Por ejemplo
lista = [6,7,8]
lista.pop(1) remueve el 7

.remove() remueve un valor de una lista

"""