#Definir una tupla con tres valores enteros. Covertir el contenido
#la tupla a tipo lista. Modificar la lista y luego convertir la lista en Tupla.
fechatupla=(25, 12, 2016)
print("Imprimimos la primer tupla")
print(fechatupla)
#copiamos la tupla en una lista
fechalista=list(fechatupla)
print("Imprimimos la lista que se le copió la tupla anterior")
print(fechalista)
#modificamos la lista
fechalista[0]=31
print("Imprimimos la lista ya modificada")
print(fechalista)
#copiamos la lista modificada a una tupla
fechatupla2=tuple(fechalista)
print("Imprimimos la segunda tupla a la que se le copió la lista")
print(fechatupla2)
