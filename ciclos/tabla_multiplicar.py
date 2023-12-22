# Tabla de Multiplicar 
# tabla_multiplicar.py
#

import os

os.system("clear")
print("\nPor favor digite un numero para desplegar su tabla de multiplicar")
numero = input()
for multiplicador in range(1,11):
    print(""+numero+" * "+str(multiplicador)+" = "+str(int(numero)*int(multiplicador)))