cadena = input("Ingrese una cadena: ")
cant = 0
for car in cadena:
    if car == "a":
        cant = cant + 1
print("La cadena tiene " + str(cant) + " letras \"a\"")