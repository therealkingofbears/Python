"""
Comentario encerrado entre triple comilla - convención de nombres de variables en Python es snake_case
"""

anio_actual = 2023

#Entrada (comentario de línean con el numeral)
anio_nacimiento = int(input("En que anio naciste?")) #input se usa para pedir un ingreso de datos por consola al usuario; int convierte el input a número entero

#Proceso
edad = anio_actual - anio_nacimiento

#Salida
print("Tu edad es", str(edad), "o", str((edad-1)), "años")
