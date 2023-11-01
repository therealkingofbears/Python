nota_min = 1
nota_max = 10

mensaje = f"¿Tu nota de examen (entre {nota_min} y {nota_max})?"
nota = int(input(f" {mensaje} "))

while nota < nota_min or nota > nota_max :
    nota = int(input(f"ERROR. {mensaje}"))
print("Genial, tu nota es válida")