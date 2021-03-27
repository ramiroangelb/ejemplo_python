frase = input('Ingresa una frase: ').lower().split()
palabra = input('Ingresa una palabra a buscar en esa frase: ').lower()
cant = 0
for elem in frase:
    if palabra in elem:
        cant = cant + 1
print('Esa palabra se encuentra ' + str(cant)+' cantidad de veces')