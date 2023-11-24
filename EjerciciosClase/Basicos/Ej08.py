#Crea una función que nos devuelva el dígito menos de un número

from cgitb import text
from tkinter import N
from token import NUMBER


def menorDigito(numero):
    menor = numero - ((numero//10)*10)
    


def menorDigitoString(numero):
    nums=str(numero)
    lista=[]
    for n in nums:
        lista.append(n)
        lista.sort(reverse=False)
        return lista[0]
    
print (menorDigitoString(239))

#Crea una función que muestre los dígitos de un número en orden inverso

def ordeninverso(numero):
    numeroEnTexto = str(numero)
    numeroEnLista = []
    for n in numeroEnTexto:
        numeroEnLista.append(n)
    numeroEnLista.sort(reverse=True)
    return numeroEnLista
x = 3825
print(ordeninverso(x))

#Crea una función que nos diga si un número es un palíndromo

def esPalindromo(numero):
    numeroEnTexto = str(numero)
    longitud=len(numeroEnTexto)
    for n in range(0,longitud // 2):
        if numeroEnTexto[n] != numeroEnTexto[-(n+1)]:
            return False
    return True

z = 12321
y = 123456

print(esPalindromo(z))
print(esPalindromo(y))

#*ards permite pasa un número variable de par´´ametros a una función

def suma(*args):
    valor = 0
    for n in args:
        valor += n
    return valor
print(suma(1,2,3,4))

#**kwargs permite tener un número variable de parámetros con nombre

def boletin(**asignaturas):
    for asignatura, nota in asignaturas.items():
        print(asignatura, nota)
boletin(matematicas=9, lengua=10)

#Nos pasan como argumento varios números, hay que decir si son todos pares o no
def numerosPar(*args):
    for n in args:
        if n % 2 != 0:
            return False
    return True
print(numerosPar(2,6,8))

#Nos pasan como argumento varios número y nos dice el número menor
def numeroMenor(*args):
    menor=args[0]
    for n in args:
        if n < menor:
            menor = n
    return menor
print(numeroMenor(2,4,6,7,9))

#Nos pasan un número variable de nombres de alumnos y sus notas 
#devolvemos el nombre del alumno con mejor nota

def mejorNota(**kwargs):
    listaNombre = list(kwargs.keys())
    listaValores = list(kwargs.values())
    notaMejor = listaValores[0]
    nombreMejor = listaNombre[0]
    
    for nombre, nota in kwargs.items():
        if notaMejor < nota:
            notaMejor = nota
            nombreMejor = nombre
    return nombreMejor, notaMejor
    
print(mejorNota(juan=0, daniel=1, javier=0, antonio=10))

#Nos pasan parejas de nombres de campo y valores y construimos una
#consulta SQL del tipo SELECT * FROM tabla WHERE campo1='valor1' and
#campo2='valor2' ....

'''
creaSQL(nombre=antonio, poblacion=Calasparra, mote=elInformatico)

SELECT * FROM presonas WHERE nombre='antonio' and poblacion='Calasparra'
'''

def creaSQL(**kwargs):
    texto="SELECT * FROM presonas WHERE "
    for clave, valor in kwargs.items():
        if type(valor) != str:
            texto += clave + "="  + str(valor) + " AND "
        else:
            texto += clave + "='" + valor + "' AND "
    texto = texto[0:-5] + ";"
    return texto
print (creaSQL(nombre= "Antonio",poblacion="Calasparra", mote=1))