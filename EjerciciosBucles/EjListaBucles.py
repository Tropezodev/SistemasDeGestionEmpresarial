#Ej01: Pregunta 4 números al usuario y los va introduciendo en una lista. Al final, los muestra todos.
lista = [None] * 4
for n in range(0,4):
    print("Introduce un número:")
    lista[n] = int(input())
print(f"EJ01: La lista es: {lista}")

#Ej02: Similar al anterior, pero se introducen números hasta que el usuario escribe un 0.
lista2=[1]
n=0
while lista2[n] != 0:
    print("Introduce un número:")
    lista2.append(int(input()))
    n += 1
lista2.pop(0)
lista2.pop(-1)
print(f"Ej02: La lista es: {lista2}")

#Ej03: Añade al ejercicio anterior que se muestre la suma de todos los elementos de la lista.
    #Método 1:
suma2 = sum(lista2)
print(f"Ej03 - Método 1: La suma de la lista {lista2} es: {suma2}")

    #Método 2:
suma2_2 = 0
for n in range (0,len(lista2)):
    suma2_2 += lista2[n]
print(f"Ej03 - Método 2: La suma de la lista {lista2} es: {suma2_2}")

#Ej04: Multiplicación de todos los elementos de una lista.
mult4 = 1
n = 0
for n in range (0,len(lista2)):
    mult4 *= lista2[n]
print(f"Ej04: La multiplicación de la lista es: {mult4}")

#Ej05: Escribe una lista de (al menos) 5 elementos y muestra en pantalla los números que son mayores que 10.
lista5 = (2,4,7,11,24,1,57)
lista5_aux = []
n = 0
for n in range(0,len(lista5)):
    if lista5[n] > 10:
        lista5_aux.append(lista5[n])
print(F"Ej05: Los números de la lista {lista5} mayores de 10 son: {lista5_aux}")

#Ej06: Suma los números impares de una lista.
lista6 = (2,7,31,4,11,24,1,13)
lista6_aux = []
n = 0
for n in range (0,len(lista6)):
    if lista6[n] % 2 != 0:
        lista6_aux.append(lista6[n])
suma6 = sum(lista6_aux)
print(F"Ej06: La suma de los números impares de la lista {lista6} es: {suma6}")

#Ej07: Suma los números situados en las posiciones impares de una lista.
lista7 = (2,7,31,4,11,24,1,13)
suma7 = 0
n = 0
for n in range(0,len(lista7)):
    if n % 2 == 0:
        suma7 += lista7[n]
print(F"Ej07: La suma de los números situados en las posiciones impares de la lista {lista7} es: {suma7}")

#EJ08: Muestra la suma de los números colocados en las posiciones pares de una lista y, por otro lado, la suma de las posiciones impares.
lista8 = (1,1,2,3,5,8)
suma8 = 0
sumaInd8 = 0
n = 0
for n in range(0,len(lista8)):
    if n % 2 == 0:
        suma8 += lista8[n]
    else:   
        sumaInd8 += (n + 1)
print(F"Ej08: La suma de los números situados en las posiciones impares de la lista {lista8} es: {suma8}")
print(F"Ej08: La suma de los indices de las posiciones pares de la lista {lista8} es: {sumaInd8}")

#Ej09: Suma los elementos de una lista que son mayores que 10.
lista9 = (2,4,7,11,24,1)
lista9_aux = []
n = 0
for n in range(0,len(lista9)):
    if lista9[n] > 10:
        lista9_aux.append(lista9[n])
suma9 = sum(lista9_aux)
print(F"Ej09: La suma de los números mayores de 10 de la lista {lista9} son: {suma9}")