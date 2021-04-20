import csv
from collections import Counter
clasificaciones = {}
with open("/home/alumno/Escritorio/Python/DesafiosTeoria_20-4/appstore_games.csv","r") as juegos:
    csvreader = csv.reader(juegos, delimiter=',')
    #Los trato como string porque no puedo pasar a float los user rating count
    next(csvreader)
    for juego in csvreader:
        if ('es' or 'ES' in juego[12]) and (juego[7] == '0'):
            print(juego[2])
        if juego[6] != '':
            clasificaciones[juego[2]] = (int(juego[6]), juego[4])
max = dict(Counter(clasificaciones).most_common(10))
for elemento in max:
    print(f'{max[elemento][1]}')

