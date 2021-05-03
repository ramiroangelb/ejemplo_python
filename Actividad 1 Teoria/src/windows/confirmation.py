''' Manejo de la ventana confirmation ''' 

import PySimpleGUI as sg

def build():
    '''
    Construye la ventana de confirmación
    '''

    size_button = (42,2)

    layout = [
        [sg.Text('¡Se ha completado el análisis!')],
        [sg.Button('Aceptar', size = size_button, key = "Exit", pad = (5,20))]
    ]

    board = sg.Window('Analisis de datos',element_justification='c',no_titlebar=True).Layout(layout)
    return board