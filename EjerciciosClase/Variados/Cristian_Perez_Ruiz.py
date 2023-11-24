'''Ej01: Escriba un programa que encuentre todos los números que son divisibles por 7 pero que no son múltiplos de 5,
    entre 2000 y 3200 (ambos incluidos). Los números obtenidos deben imprimirse en una secuencia separada por comas en una sola línea.
    Sugerencias: Considere usar el método range(#begin, #end)'''

lista=[]
for n in range(2000,3201):
    if n % 7 == 0 and n % 5 != 0:
            lista.append(str(n))
print(", ".join(lista))

'''Ej02: Escriba un programa que pueda calcular el factorial de un número dado.
    Los resultados deben imprimirse en una secuencia separada por comas en una sola línea.
    Supongamos que se proporciona la siguiente entrada al programa: 8 Entonces, la salida debería ser: 1, 2, 6, ..., 40320
    Sugerencias: en caso de que se proporcionen datos de entrada a la pregunta, se debe suponer que se trata de una entrada de consola.'''

lista2=[]
aux2 = 1
factorial=int(input("Introduce un número para obtener el factorial: "))
for n in range(1, factorial+1):
    aux2 *= n
    lista2.append(str(aux2))
print(", ".join(lista2))

'''Ej03: Con un número entero n dado, escriba un programa para generar un diccionario que contenga (i, i*i)
    tal que sea un número entero entre 1 y n (ambos incluidos). Luego el programa debería imprimir el diccionario.
    Supongamos que se proporciona la siguiente entrada al programa: 8
    Entonces, la salida debería ser: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64 }'''


numero3 = int(input('Introduce un número para crear el diccionario (i, i*i): '))
diccionario3 = {}
for n in range(1, numero3+1):
     diccionario3[n] = n * n
print(diccionario3)

'''Ej04: Escriba un programa que acepte una secuencia de números separados por comas
    desde la consola y genere una lista y una tupla que contenga cada número.
    Supongamos que se proporciona la siguiente entrada al programa: 34,67,55,33,12,98
    Entonces, la salida debería ser: ['34', '67', '55', '33', '12', ' 98'] ('34', '67', '55', '33', '12', '98')
    Sugerencias: en caso de que se proporcionen datos de entrada a la pregunta, se
    debe suponer que se trata de una entrada de consola . El método tuple () puede
    convertir la lista en tupla'''

numeros4 = input('Introduce varios números separados por ",": ')
lista4 = numeros4.split(",")
lista4Tupla = tuple(lista4)
print(f"{lista4} : {lista4Tupla}")

'''Ej05:Escriba un programa que acepte una secuencia de palabras separadas por comas como
    entrada e imprima las palabras en una secuencia separada por comas después de ordenarlas alfabéticamente.
    Supongamos que se proporciona la siguiente entrada al programa: sin,hola,bolsa,mundo
    Entonces la salida debería ser: bolsa,hola,sin,mundo.
    Sugerencias: en caso de que se proporcionen datos de entrada a la pregunta, se debe
    suponer que se trata de una entrada de consola. Puedes usar el método sort.'''

cadena5 = input('Introduce varias palabras separadas por ",": ')
lista5 = cadena5.split(",")
print(sorted(lista5))

'''Ej06: Escriba un programa que acepte una secuencia de líneas como entrada e imprima las
    líneas después de poner todos los caracteres de la oración en mayúscula.
    Supongamos que se proporciona la siguiente entrada al programa: Hola mundo La práctica hace la perfección
    Entonces, la salida debería ser: HOLA MUNDO LA PRÁCTICA HACE LA PERFECCIÓN
    Sugerencias: en caso de que se proporcionen datos de entrada a la pregunta, se debe suponer que se trata de una entrada de consola.
    Debe pedir cadenas hasta que se introduzca la cadena vacía'''

linea = ["a"]
lineaUpper = []
n = 0
while linea[n] != "":
    linea[n] = input("Introduce una línea: ")
    lineaUpper.append(linea[n].upper())
    +n    
print(" ".join(lineaUpper))