"""
def doble(n):
    return n * 2
"""


lista = [1,2,3,4]
nombres = ["Juan", "Diego", "Matías"]

#print(list(map(doble, lista)))

print(list(map(lambda x : x * 2, lista))) #el último término de la función (en este caso "lista", es la variable donde se van a alojar los resultados de la función lambda)
print(list(map(lambda nom : nom.upper(), nombres)))
