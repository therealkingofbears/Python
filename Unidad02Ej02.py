#FUNCION
def fecha_valida(dia, mes, anio):
    if mes in {4, 6, 9, 11}:
        max_dias = 30
    elif mes == 2:
        if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
            max_dias = 29  # Año bisiesto
        else:
            max_dias = 28
    else:
        max_dias = 31
    
    if dia > max_dias:
        return False
    else:
        return True


#PRINCIPAL
dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
anio = int(input("Ingrese el año: "))

if fecha_valida(dia, mes, anio):
    print("La fecha es válida.")
else:
    print("La fecha no es válida.")
