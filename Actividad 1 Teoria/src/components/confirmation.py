''' Manejo de eventos en la ventana confirmation '''

import PySimpleGUI as sg
from src.windows import confirmation

def start():
    '''
    Abre la ventana de confirmación
    '''
    window = loop()
    window.close()
    

def loop():
    '''
    Loop de la ventana de confirmación que espera a ser cerrada
    '''
    window = confirmation.build()

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED,"Exit") or event == "Exit":
            break
    return window