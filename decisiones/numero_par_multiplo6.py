#numero_par_multiplo6

import os
import math

numero = 0

while numero == 0:
    os.system("clear")
    print("\nDigite un valor númerico")
    numero = input()
    if int(numero) % 2 == 0:
        if int(numero) % 6 == 0:
            print("el numero es par y multiplo de 6")
        else:
            print("\n el numero es par, pero no multiplo de 6")
numero = 0    
print("\n Presione ENTER para continuar")
x=input()
  
