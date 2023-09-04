#Desarrollar una aplicación que nos permita crear un diccionario
#inglés/castelano. La clave es la palabra en inglés y el valor
#es la palabra en castellano.
#Crear las siguientes funciones:
#1) Cargar el diccionario.
#2) Listado completo del diccionario.
#3) Ingresar por el teclado una palabra en inglés y si existe en el diccionario.

def cargar():
    diccionario={}
    continúa="s"
    while continúa=="s":
        caste=input("Ingrese una palabra en castellano:")
        ing=input("Ingrese una palabra en inglés:")
        diccionario[ing]=caste
        continúa=input("¿Quiere cargar otra palabra?:[s/n]")
    return diccionario


def imprimir(diccionario):
    print("Listado completo del diccionario")
    for inglés in diccionario:
        print(inglés,diccionario[inglés])


def consulta_palabra(diccionario):
    pal=input("Ingrese la palabra en inglés a consultar:")
    if pal in diccionario:
        print("En castellano significa:",diccionario[pal])


#bloque principal

diccionario=cargar()
imprimir(diccionario)
consulta_palabra(diccionario)
