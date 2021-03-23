print("Ingresa una palabra y te dirà si comienza y termina con la misma letra (¡Hay diferencia entre mayuscula y minuscula!)")
cadena = input("Ingresà una palabra: ")
lista = []
while cadena != "FIN":
    lista.append(cadena)
    cadena = input("Ingresà una palabra: ")
for palabra in lista:
    if palabra[0] == palabra[-1]:
        print(palabra + " empieza y termina con la misma letra")
