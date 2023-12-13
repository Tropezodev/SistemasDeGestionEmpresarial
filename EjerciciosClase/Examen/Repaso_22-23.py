'''
1. Partiendo de una lista como [36, 25, 32, 48, 127] indica la cantidad de números que son múltiplos de 3 y 4 simultáneamente.
El programa debe funcionar independientemente de la longitud que tenga la lista de números.
'''

def ej01 (lista):
    multiplos3=[]
    multiplos4=[]
    for n in range (len(lista)-1):
        if (lista[n] % 3 == 0):
            multiplos3.append(lista[n])
        if (lista[n] % 4 == 0):
            multiplos4.append(lista[n])
    print(f"Los múltiplos de 3 son: {multiplos3}")
    print(f"Los múltiplos de 4 son: {multiplos4}")

lista = [3,4,6,8,12,120,30,40]

'''
2. En las siguientes listas tenemos los nombres de los rivales en los partidos de España en el Mundial en la fase de grupos,
los goles que ha marcado España en cada partido y los goles que han marcado los rivales:
    a. rivales=["Costa Rica", "Alemania", "Japón"]
    b. golesAFavor=[7, 1, 2]
    c. golesEnContra=[0, 1, 0] #El resultado del partido contra Japón solo es un pronóstico
Crea un programa que indique lo siguiente teniendo en cuenta los valores de las listas anteriores (El programa debe seguir funcionando correctamente si los datos
cambian o se amplían):
    ● Partidos jugados
    ● Partidos ganados
    ● Partidos empatados
    ● Partidos perdidos
    ● Goles a favor
    ● Goles en contra
    ● Diferencia de goles
    ● Puntos totales conseguidos por España.
    ● NOTA: Por cada partido ganado se consiguen 3 puntos, por cada partido empatado 1 punto y por cada partido perdido 0 puntos.
    ● NOTA2: Por si alguien no lo tiene claro, en fútbol gana el equipo que mete más goles. En caso de que los dos equipos consigan los mismos goles, se produce un empate.
'''

def ej02 (rivales,listaGolesFavor, listaGolesContra):
    pJugados=len(rivales)
    gFavor=sum(listaGolesFavor)
    gContra=sum(listaGolesContra)
    gDiferencia=gFavor-gContra
    
    pGanados = 0
    pPerdidos = 0
    pEmpatados = 0
    puntos = 0
    
    for n in range(len(rivales)):
        if (listaGolesFavor[n]>listaGolesContra[n]):
            pGanados+=1
            puntos+=3
        elif (listaGolesFavor[n]<listaGolesContra[n]):
            pPerdidos+=1
        else:
            pEmpatados+=1
            puntos+=1
    print(f"España ha jugado {pJugados} partidos.")
    print(f"España ha ganado {pGanados} partidos.")
    print(f"España ha empatado {pEmpatados} partidos.")
    print(f"España ha perdido {pPerdidos} partidos.")
    print(f"España ha marcado {gFavor} goles.")
    print(f"España ha recibido {gContra} goles.")
    print(f"La diferencia de goles es de {gDiferencia}.")
    print(f"España ha conseguido {puntos} puntos.")

rivales = ["Costa Rica", "Alemania", "Japón"]
golesAFavor = [7, 1, 2]
golesEnContra = [0, 1, 0]

'''
3. En el siguiente diccionario tienes una lista de países y capitales.
Crea un programa que pregunte al usuario el nombre de un país y después el de su capital y lo añada al diccionario:
    a. capitales={"España":"Madrid", "Italia":"Roma", "Francia":"París"}
Después debe mostrar lo siguiente usando el diccionario:
    ● Madrid capital de España
    ● Roma capital de Italia
    ● París capital de Francia
'''

def ej03 ():
    capitales = {"España":"Madrid", "Italia":"Roma", "Francia":"París"}
    pais = input("Introduce un pais:")
    capitales [pais] = input("Introdice su capital:")
    print()
    for key, value in capitales.items():
        print(f"{value} capital de {key}")


'''
4. (Punto adicional) Modifica el programa anterior para que se pidan nuevos países y capitales hasta que se introduzca un 0 en el país.
'''

def ej04():
    capitales = {"España":"Madrid", "Italia":"Roma", "Francia":"París"}
    while (True):
    #while ("0" not in capitales):
        pais = input("Introduce un pais (introduce 0 para terminar):")
        if (pais == "0"):
            break
        else:
            capitales [pais] = input("Introdice su capital:")
            print()
    print()
    for key, value in capitales.items():
        print(f"{value} capital de {key}")
        

# -------------------------- Llamada a las Funciones -------------------------- #

#ej01(lista)
#ej02(rivales, golesAFavor, golesEnContra)
#ej03()
#ej04()