''' Manejo interno del dataset1 '''

import csv
import json

def dataset_analisis():
    ''' Analisis del dataset1. Escribe en un archivo los datos a procesar '''

    #Analisis de proyectos mineros con ubicación aproximada
    #Licencia sin aclarar // datos Argentina
    #Dato a analizar: Obtener el nombre de la mina y empresa encargada al lugar de toda ubicación que mine plata.

    archivo = open('src/datasets/proyectos-mineros-ubicacin-aproximada-.csv','r',encoding = 'utf-8')
    csv_reader = csv.reader(archivo, delimiter = ',')

    next(csv_reader) #Ignoro la primera línea
    
    #i[1] es nombre de la mina
    #i[2] es empresa encargada al lugar
    #i[5] es el mineral extraído del lugar

    dic = {}
    indice_dic = 0

    for i in csv_reader:
        if i[5] == 'Plata':
            indice_dic += 1
            dic[indice_dic] = {'Nombre': i[1], 'Empresa': i[2], 'Mineral': i[5]}
    archivo.close()

    archivo_json = open('resultado_dataset1.txt','w')
    json.dump(dic,archivo_json, indent=4)
    archivo_json.close()