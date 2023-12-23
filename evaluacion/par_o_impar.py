# número par o impar


# perdón, no me alcanzó el tiempo.

import os
import math

def numero_Primo(numero):
    if int(numero) == 0 or int(numero) == 1:
        return False
    if int(numero) / 1 == int(numero) and int(numero) / int(numero) == 1:
        return True
    
def numero_Par(numero):
    if int(numero) % 2 == 0:
        return True
    return False

control = 0
while control == 0:
    
    os.system("clear")
    print("\nDigite un número , cero para finalizar")
    numero = input()
    if int(numero) == 0:
        break
    if numero_Par(numero) == True:
        print("\n Numero es par "+str(numero))
    es_Primo = numero_Primo(numero)
    if es_Primo == True:
        print("\n Numero es primo")
    
    if int(numero)%2 == 0:  # si es par
        print ("es par")
        if int(numero)/int(numero) == 1 and int(numero)/1 == int(numero):
            print("El número "+str(numero)+" es par y primo")
    print("\n numero"+numero)
    print("\n Presione <ENTER> para continuar")
    x = input()