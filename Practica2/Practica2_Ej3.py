texto = ''' Wikipedia:
Game Boy (Japonés: ゲームボーイ "Gēmu Bōi") es una videoconsola portátil desarrollada y comercializada por Nintendo,
 lanzada por primera vez en Japón y América del Norte en 1989, y en Europa un año después. 
 Perteneció a la línea de consolas Game Boy, siendo esta la primera de la serie.
'''
print(texto)
texto = texto.lower()
texto = texto.split()
contadorPalabras = 0
letra = input("Ingresa una letra, yo contaré la cantidad de palabras que empiecen con ella: ")

while True:
    letra = letra.lower()
    if letra.isalpha() and len(letra) == 1:
        #Si es una letra...
        for palabra in texto:
            if palabra.startswith(letra):
                contadorPalabras = contadorPalabras+1
        break #Utilizo break porque lo he visto en el hangman y lo comprendí al verlo ejecutarse

    else:
        #Si NO es una letra...
        print('¡Eso no es una letra!')
        letra = input("Ingresa una letra, yo contaré la cantidad de palabras que empiecen con ella: ")

print('Hay '+str(contadorPalabras)+' palabras que tienen '+'\"'+ str(letra.upper()) +'\"'+' como su primera letra.')