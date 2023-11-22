#Ej01: Pregunta 4 números al usuario y los va introduciendo en una lista. Al final, los muestra todos.

lista=[None] * 4
for n in range(0,4):
    print("Introduce un número:")
    lista[n]=int(input())
print(lista)

#Ej02: Similar al anterior, pero se introducen números hasta que el usuario escribe un 0.

