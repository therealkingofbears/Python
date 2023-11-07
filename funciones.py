# DEFINICIÓN DE FUNCIONES

def siguiente(n): # def es la palabra reservada para definir una función
    # instrucción que pertenece a la función
    sig = n + 1
    return sig # La palabra reservada "return" se usa para devolver un valor

# No pertenece a la función, en Java la función está definida dentro de la indentación

def es_vocal(letra):
    return letra in "AEIOUaeiou"

# PROGRAMA PRINCIPAL

print( es_vocal('a'))