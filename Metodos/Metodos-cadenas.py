cadena1 = "Hola soy dalto"
cadena2 = "Bienvenido maquinola"

#convierte a mayasculas
mayusc = cadena1.upper()

#convierte a minusculas
minusc = cadena1.lower()

#Primera letra en mayuscula
primer_letra_mayusc = cadena1.capitalize

#buscamos una cadena en otra cadena, si no hay coincidencias devuelve -1
busqueda_find = cadena1.find("a")

#buscamos una cadena en otra cadena, scadena1.index("a")i no hay coincidencias lanza una excepcion (error) 
busqueda_index = cadena1.index("a")

#si es numerico, devolvemos True, sino devolvemos False
es_numerico = cadena1.isnumeric()

#si es alfa numerico devlvemos True, sino devolvemos False
es_alfanumerico = cadena1.isalpha()

#contamos las coincidencias de una cadena, dentro de otra cadena, devuelve la cantidad de coincidencias
contar_coincidencias = cadena1.count("a")

#contamos cuantos caracteres tiene una cadena
contar_caracterees = len(cadena1)

#verificamos si una cadena empieza con otra cadena dada, si es asi devuelve True
empieza_con = cadena1.startswith("H")

#verificamos si una cadena termina con otra cadena dada, si es asi devuelve True
termina_con = cadena1.endswith("H")

#si el valor 1, se encuentra en la cadena original, reemplaza el valor 1 de la misma, por el valor 2
cadena_nueva = cadena1.replace("la", "lu")

#separar cadenas con la cadena que le pasemos
cadena_separada = cadena1.split(",")

print()