frase = '''
Esto es UN un texto con CON cosas repetidas REPETIDAS y al que tengo QUE modificar MODIFICAR
 para poner EN MINUSCULAS y SACAR SACAR palabras que sean REPETIDAS
'''.lower().split()
lista = []

for palabra in frase:
    if palabra not in lista:
        lista.append(palabra)
print(lista)