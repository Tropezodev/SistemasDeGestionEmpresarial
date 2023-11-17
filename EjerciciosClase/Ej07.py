
#Función Suma

def suma(numero1, numero2):
    return numero1+numero2
    
print(suma(1,27))

#Función Resta
def resta(numero1, numero2):
    return numero1-numero2
    
print(resta(1,27))

#Raiz cuadrada
import math
print(round(math.sqrt(7),3))

'''
#Librería para leer webs
import urllib.request
u = urllib.request.urlopen('https://www.laverdad.es/')
print(u.read())
'''

#Función Saludar
def saludar(nombre,saludo="Hola",pais="España"):
    print(saludo,nombre,pais)
    
saludar("Andrea")
saludar("Gabriel","Buenos días")
saludar("Jose Antonio",pais="Mozambique")

#Función importe del IVA
def calculaIVA(precio,iva=0.21):
    importeIVA=precio*iva
    return importeIVA
print("El importe del IVA es:", round(calculaIVA(100)))

#Función precio con IVA
def precioConIVA(precio):
    total=precio*1.21
    #total=precio+precio*0.21
    return(total)
print("El precio con IVA es:", round(precioConIVA(100)))

#Función quitar IVA
def precioSinIVA(precio):
    total=precio/1.21
    return(total)
print("El precio sin IVA es:", round(precioSinIVA(121)))