#El enunciado es confuso en cuanto a lo que pasarìa si introduzco 30, por lo que usarè if X else X if X -- Sin usar if elif

num = int(input("Ingrese un numero: "))
if num % 2 == 0:
    print("Es Multiplo de 2")
else:
    print("No es multiplo de 2")
if num % 3 == 0:
    print("Es Multiplo de 3")
else:
    print("No es multiplo de 3")
if num % 5 == 0:
    print ("Es multiplo de 5")
else:
    print ("No es multiplo de 5")    