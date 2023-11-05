# Te piden 3 nombres y los muestras ordenados por pantalla alfabéticamente:
lista=[]
for n in range(3):
    nombre=input("Dime un nombre: ")
    lista.append(nombre)
print(sorted(lista))