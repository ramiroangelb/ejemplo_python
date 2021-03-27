def calcularValorPalabra(cadena):
    total = 0
    for letra in cadena:
        if letra in diccionario[1]:
            total = total + 1
        elif letra in diccionario[2]:
            total = total + 2
        elif letra in diccionario[3]:
            total = total + 3
        elif letra in diccionario[4]:
            total = total + 4
        elif letra in diccionario[5]:
            total = total + 5
        elif letra in diccionario[8]:
            total = total + 8
    return total

diccionario = {1: ('a','e','i','o','u','l','n','r','s','t'),
2: ('d','g'),
3: ('b','c','m','p'),
4: ('f','h','v','w','y'),
5: ('k'),
8: ('j','x'),
10: ('q','z')}

cadena = input("Ingresa una palabra, yo te daré su valor según Scrabble")
print(f"Tu puntaje fue de: {calcularValorPalabra(cadena)}")