# Nos pide tres números y hace la suma y nos muestra el resultado
lista=[]
suma=0
for n in range(3):
    numero=int(input("Dime un número: "))
    lista.append(numero)
    suma+=lista[n]
print("La suma de", lista, " es ", suma)