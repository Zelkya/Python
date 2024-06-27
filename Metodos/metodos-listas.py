#creando una lista con list()
lista = list(["hola", "dalto", 34])

#devuelve la cantidad de elementos de la lista
cantidad_elemntos = len(lista)

#agregando un elemento a la lista
lista.append("JAJAJJAJ")

#agregando un elemento a la lista en un indice especifico
lista.insert(2, "TOMA MAMA")

#agregando varios elementos a la lista
lista.extend([False, 2030])

#eliminando un elemento de la lista (por su indice) (si pones -1 se elimina el ultimo dato de la lista y -2 para eliminar el anteultimo y asi sucesivamente)
lista.pop(0)

#removiendo un elemento de la lista por su valor
lista.remove("TOMA MAMA")

#eliminando todos los elementos de la lista
lista.clear()

#ordenando la lista de forma ascendente (si usamos el parametro reverse=True lo ordena en reversa)
lista.sort()

#invirtiendo los elementos de una lista
lista.reverse()

#verificando si un elemento esta en la lista
elemento_encontrado = lista.index(56)
