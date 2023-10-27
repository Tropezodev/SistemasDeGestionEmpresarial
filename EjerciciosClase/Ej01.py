#EJERCICIOS
#1
L = ["Grabiel","Andlea","Yisus","Miguel Barbel","Jean Culero"]
print(L)

#2
L.insert(3,"Peblo")
print(L)

#3
L.sort()
print(L)

#4
L.append("Antonio")
print(L)

#5
L.insert(0,"Rigoberta")
print(L)

#6
print(L.index("Antonio"))

#7
L.sort()
print(L)

#8
L.insert(L.index("Rigoberta")+1,"Merche")
print(L)

#9
for n in range(0,len(L)):
	print(n,":", L[n])
print("\n")
for alumno in L:
	print(L.index(alumno),":", alumno)