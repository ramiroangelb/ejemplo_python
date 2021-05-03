''' Manejo interno del dataset2 '''

import csv
import json

def dataset_analisis():
    ''' Analisis del dataset2. Escribe en un archivo los datos a procesar '''

    #Análisis de uso de drogas por edad
    #Licencia sin aclarar // datos Argentina
    #Dato a analizar: Obtener grupo del reclamo, mes (nombre de mes) y provincia de todo reclamo hecho desde vía 'TELEFONICO'

    archivo = open('src/datasets/reclamos_prestadoras_2020.csv','r',encoding = 'utf-8')
    csv_reader = csv.reader(archivo, delimiter = ',')

    next(csv_reader) #Ignoro la primera línea

    #i[2] es nombre de mes
    #i[4] es provincia
    #i[5] es grupo del reclamo
    #i[6] es via de ingreso

    dic = {}
    indice_dic = 0

    for i in csv_reader:
        if i[6] == 'TELEFONICO':
            indice_dic += 1
            dic[indice_dic] = {'Mes': i[2], 'Provincia': i[4], 'Grupo reclamo': i[5], 'Via de ingreso': i[6]}
    archivo.close()


    archivo_json = open('resultado_dataset2.txt','w')
    json.dump(dic,archivo_json, indent=4)
    archivo_json.close()
