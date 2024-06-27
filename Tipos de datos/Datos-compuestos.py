#Creando una lista (se puede modificar)
lista = ["Lucas Dalto", "Soy dalto",True,1.85]

#Creando una tupla (no se puede modificar)
tupla = ("Lucas Dalto", "Soy dalto",True,1.85)

#Esto es valido
lista[3] = "Maquinola"

#esto no
#tupla[3] = "Maquinola"

#Creando un conjunto (set) (no accede a elementos por indice, no almacena datos duplicados)

conjunto = {"Lucas Dalto", "Soy dalto",True,1.85}

#print(conjunto[3]) -> no se puede acceder al elemento

#creando un diccionario (dict) (la estructura es key: value y separamos con comas)
diccionario = {
    'nombre' : "Lucas Dalto",
    'Canal' : "Soy Dalto",
    'esta_emocionado' : "True",
    'altura' : "1.84",
    'dato_duplicado' : "Soy dalto",
}
print(diccionario['Canal'])