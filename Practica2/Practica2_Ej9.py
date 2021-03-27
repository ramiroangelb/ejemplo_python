def esHeterograma(cadena):
    heterograma = True
    for letra in cadena.lower():
        if letra.isalpha:
            if cadena.count(letra) > 1:
                heterograma = False
                break
    return heterograma


cadena = input("Inserte una palabra o frase y le diré si es un heterograma: ")
if esHeterograma(cadena):
    print("¡Sí, es heterograma!")
else:
    print("¡No, no es heterograma!")