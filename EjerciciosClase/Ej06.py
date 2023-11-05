def convertirCSV(nombre_archivo):
    separador=","
    archivo = open(nombre_archivo, encoding="utf-8")
    next(archivo)
    usuarios = []
    for linea in archivo:
        linea = linea.rstrip("\n")
        columnas = linea.split(separador)
        QuotaAmount = int(columnas[0])
        StartDate = str(columnas[1])
        OwnerName = str(columnas[2])
        Username = str(columnas[3])
        usuarios.append({
            "QuotaAmount" : QuotaAmount,
            "StartDate" : StartDate,
            "OwnerName" : OwnerName,
            "Username" : Username,
        })
    return usuarios
documento = convertirCSV("Ej06.csv")
print(documento)