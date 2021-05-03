''' Manejo de eventos en la ventana main '''

import PySimpleGUI as sg
from src.windows import main
from src.components import confirmation
from src.functions import dataset1 as d1
from src.functions import dataset2 as d2

def start():
    '''
    Abre la ventana de inicio
    '''
    window = loop()
    window.close()
    

def loop():
    '''
    Loop de la ventana de inicio que espera la selección de
    algún dataset para analizar
    '''
    window = main.build()

    while True:
        event, values = window.read()
        if event == "Exit":
            print('Evento: ' + event)
            break
        elif event == "Analisis1":
            d1.dataset_analisis()
        elif event == "Analisis2":
            d2.dataset_analisis()
        print('Evento: ' + event)
        confirmation.start()
    return window