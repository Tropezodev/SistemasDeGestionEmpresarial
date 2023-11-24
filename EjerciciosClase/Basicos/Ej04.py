# Nos pide 4 números y después nos pregunta qué operación quiere hacer sumar (+) o multiplicar (*)
lista=[]
total=0
for n in range(4):
    lista.append(int(input("Dime un número: ")))

total=input("Dime si quieres sumar (+) o multiplicar (*): ")

if total=="+":
    total=0
    for numero in lista:
        total += numero
    print("El total es ", total)
elif total=="*":
    total=1
    
    for numero in lista:
        total*=numero
    print("El total es ", total)
else:
    print("Operación no definida")