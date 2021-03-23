cadena1 = input("Ingrese la cadena 1:  ")
cadena2 = input("Ingrese la cadena 2:  ")
if len(cadena1) > len(cadena2):
    print("La cadena más larga es: " + cadena1)
elif len(cadena1) < len(cadena2):
    print("La cadena más larga es: " + cadena2)
else:
    print("Las cadenas son iguales")