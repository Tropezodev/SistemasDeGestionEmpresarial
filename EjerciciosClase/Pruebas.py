"""linea="1; Benito Camleas; Calle tano,34; 30180; Calasparra; Murcia"
lista=linea.split(";")
print(lista)

for l in lista:
    print(l)

lista2=["Argentina", "Francia", "Italia", "Croacia"]
print("Daniel" in lista)

pais=input("Dime un país: ")

if pais not in lista2:
    lista2.append(pais)

print(lista2)

pais=input("Dime un el pais del que quieres saber la posición: ")
if pais not in lista2:
    print("El país no está en los 4 primeros")
else:
    print(lista2.index(pais)+1)"""

suspensos=["Juan", "Pedro", "Paco", "Antonio"]
suspensos.remove("Juan")
print(suspensos)
#suspensos.sort()
#print(suspensos)
print(sorted(suspensos))