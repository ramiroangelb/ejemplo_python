#Ingresar las notas
#Calcular promedio
#Calcular cuantos tienen notas menores al promedio
######Comienzo a usar funciones

def leerDatos(lista):
    """ Esta funciòn llena una lista con numeros """
    nota = int(input("Ingresà una nota: "))
    while nota != -1:
        lista.append(nota)
        nota = int(input("Ingresà otra nota: "))

def calcularPromedio(lista):
    """ Esta funciòn calcula el promedio desde una lista """
    suma = 0
    for elem in lista:
        suma = suma + elem
    return suma / len(lista)

def notasMenoresAlPromedio(promedio):
    """ Esta funciòn saca la cantidad de numeros menores a otro numero """
    cant = 0
    for elem in lista:
        if elem < promedio:
            cant = cant + 1
    return cant

lista = []



leerDatos(lista)
promedio = calcularPromedio(lista)
cantNotasMenoresAlPromedio = notasMenoresAlPromedio(promedio)

#Podrìa llamar a la funciòn dentro del print pero
#usè variables para entender bien què pasa por el momento
print("La lista està conformada por: "+ str(lista))
print("El promedio es: " + str(promedio))
print("Las notas menores al promedio son: " + str(cantNotasMenoresAlPromedio))
