#Ej01: Bart Simpson tiene que escribir 10 veces "Hoy me voy a portar bien en clase".
for n in range(10):
    print("Hoy me voy a portar bien en clase")
    
#Ej02: Mostrar los números del 1 al 100.
for n in range(1,101):
    print(n)
    
#Ej03: Lo mismo de 5 en 5.
for n in range (0,101,5):
    print(n)
    
#Ej04: Mostrar los números del 10 al 1.
for n in range (10,0,-1):
    print(n)
    
#Ej05 Tabla de multiplicar de un número que se pregunta al usuario.
print("Introduce un número:")
numero=int(input())
for n in range(0,11):
    print(f"{n} x {numero} = {n*numero}")
    
#Ej06: Pregunto números y los voy sumando hasta que introducen un cero.
numero=1
suma=0
while numero !=0:
    print("Introduce un número (0 para terminar):")
    numero=int(input())
    suma+=numero
    print(f"La suma es: {suma}")
    
#Ej07: Calcula el factorial de un número.
print("Introduce un número:")
numero=int(input())
factorial=1
for n in range(1,numero+1):
    factorial*=n
print(f"El factorial de !{numero}= {factorial}")

#Ej08: Pregunta cinco números y cuando un número sea negativo, muestra en pantalla el mensaje "es negativo"
for n in range(0,5):
    print("Introduce un número:")
    numero=float(input())
    if (numero<0):
        print(f"El número es {numero} negativo.")
        
#Ej09: Pregunta números hasta que se introduce un cero y nos dice cuál es el máximo.
numero=1
aux=0
while numero !=0:
    print("Introduce un número (0 para terminar):")
    numero=int(input())
    if numero>aux:
        aux=numero
print(f"El número mayor es: {aux}")