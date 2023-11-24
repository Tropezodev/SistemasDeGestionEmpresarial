# Tienes un número secreto aleatorio (0-10) y te pide que escribas un número hasta que lo aciertes
import random

numeroSecreto=random.randint(0,10)
minumero=int(input("Dime un número: "))

while numeroSecreto!=minumero:
    if numeroSecreto>minumero:
        print("El número secreto es mayor.")
    else:
        print("El número secreto es menor.")
    minumero=int(input("Dime un número: ")) 

print("Acertaste! El número secreto es: ", numeroSecreto)