risa = 'ja'
carcajada = risa*5 #se puede multiplicar una cadena para concatenarla
asteriscos = '*'*10
print(f"{carcajada}")
print(f"{asteriscos}")

#La triple comilla sirve para poder escribir cadenas con espacios y líneas tal y cual las escribo entre las triple cadenas
cadena1 = """En Python es posible definir
cadenas de caracteres utilizando más de una
línea de código"""

print(f"{cadena1}")

#concatenación de cadenas

var1 = 3 + 5 #esto es una suma de números enteros
var2 = "3" + "5" #esto va a dar 35 porque concatena dos cadenas de texto

print(f"{var1}" , f"{var2}")

#comparación de cadenas
cadena1 = "Hola"
cadena2 = "Codo a Codo"
print(cadena1 > cadena2) #va a comparar los strings y va a devolver un valor lógico; en este caso true - La comparación es una prueba lógica
print(cadena1 == cadena2) #va a comparar los strings y va a devolver un valor lógico; en este caso false - La comparación es una prueba lógica

#Longitud con la función len
nombre = "Codo a Codo"
print(len(nombre)) #se imprime 11 que es la longitud de la cadena dentro de la variable "nombre"

#Métodos de cadenas
cadena = "Codo a Codo"
print(cadena.upper) #devuelve en upper case
print(cadena.lower) #devuelve en lower case
print(cadena.capitalize) #usa mayúscula en la primera letra de cada palabra de la cadena

#Rebanar cadenas
cadena = "Hola mundo!"
print(cadena[6:11]) # va a imprimir "mundo", porque le damos las posiciones de cada letra para imprimir

#iterar en cadena
cadena = "Python"
for letra in cadena:
    print(letra)
