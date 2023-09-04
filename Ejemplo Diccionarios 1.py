#En el bloque principal del programa definir un diccionario que almacene
#los nombres de países como clave y como valor la cantidad de habitantes.
#Implementar una función para mostrar cada clave y valor.
def imprimir(países):
    for clave in países:
        print(clave, países[clave])


#bloque principal

países={"Argentina":40000000, "España":46000000, "Brasil":190000000, "Uruguay": 3400000}
imprimir(países)
