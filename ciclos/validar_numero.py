
import os

numero = 1
while numero != 0:
    os.system("clear")
    print("\nFavor digite un valor numérico, cero (0) para salir")
    numero = input()
    if int(numero) > 0:
        print("El número es "+numero)
    else:
        if int(numero) == 0:
            break
        else:
            print("el numero no es un valor positivo superior a cero ")
    print ("\nPresione <ENTER> para continuar")
    x=input()