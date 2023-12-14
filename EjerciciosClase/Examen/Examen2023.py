#Ej13
def ej13(lista):
    listaSuma=[]
    media=0
    for n in range (len(lista)):
        if (10 < lista[n] < 60):
            listaSuma.append(lista[n])
    print(f"La suma de las edades entre 10-60 es: {sum(listaSuma)}")
    if (sum(listaSuma) == 0):
        print("La media de las edades entre 10-60 es: 0")
    else:
        media=sum(listaSuma)/len(listaSuma)
        print(f"La media de las edades entre 10-60 es: {media}")

#Ej14
def ej14():
    palabra=input("Introduzca una palabra:")
    for letra in palabra:
        print(letra, end=" ")
    print()

#Ej15
def ej15(lista):
    mayor=lista[0]
    menor=lista[0]
    for n in range (len(lista)):
        if (n < lista[n]):
            mayor=lista[n]
        if (n > lista[n]):
            menor=lista[n]
    print(f"El número mayor es: {mayor}\nEl número menor es: {menor}")

#Ej16
def ej16():
    edades={"Antonio":29,"María":19,"Roberto":21}
    nombre=input("Introduzca el nombre:")
    edades[nombre]=input("Introduce la edad:")
    print()
    for key, value in edades.items():
        print(f"{key} tiene {value} años.")


# -------------------------- Llamada a las Funciones -------------------------- #

#ej13([34,25,32,48,120])
#ej14()
#ej15([34,25,32,48,120,-1])
#ej16()