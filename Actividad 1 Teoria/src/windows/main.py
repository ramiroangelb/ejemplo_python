''' Manejo de la ventana main '''

import PySimpleGUI as sg

def build():
    '''
    Construye la ventana de inicio
    '''

    size_button = (42,2)

    layout = [
        [sg.Text('¡Selecciona un dataset a analizar!')],
        [sg.Button('Proyectos mineros ubicación aproximada', size = size_button, key = "Analisis1")],
        [sg.Button('Reclamos prestadoras 2020', size = size_button, key = "Analisis2")],
        [sg.Button('Salir', size = size_button, key = "Exit", pad = (5,25))]
    ]

    board = sg.Window('Analisis de datos',element_justification='c',no_titlebar=True).Layout(layout)
    return board