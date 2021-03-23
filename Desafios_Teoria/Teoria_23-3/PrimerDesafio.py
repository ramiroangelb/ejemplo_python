#Soluciòn 1
for i in range(4):
    cadena = input("Ingresà una cadena")
    if "r" in cadena:
        print("TIENE R")
    else:
        print("NO TIENE R")
#Soluciòn 2
for i in range(4):
    cadena = input("Ingresà una cadena")
    mensaje = "TIENE R" if "r" in cadena else "NO TIENE R"