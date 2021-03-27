cadena = input('Ingresa la clave (debe tener menos de 10 caracteres y no contener los simbolos @ y !): ')
if len(cadena) > 10:
    print('Ingresaste más de 10 caracteres')
cant = 0
if cadena.startswith('@') or cadena.endswith('!'):
    print('Ingresaste alguno de estos simbolos: @ o !')
else:
    print("Ingreso OK <3")