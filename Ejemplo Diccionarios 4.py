#Confeccionar un programa que permita cargar un código de producto como
#clave de un diccionario. Guardar para dicha clave el nombre del producto,
#su precio y cantidad en stock.
#Implementar las siguientes actividades:
#1) Carga de datos en el diccionario.
#2) Listado completo de productos
#3) Consulta de un producto por su clave, mostrar el nombre, precio y stock.
#4) Listado de tododos los productos que tengan un stock con valor cero.

def cargar():
    productos={}
    continua="s"
    while continua=="s":
        código=int(input("Ingrese el código del producto:"))
        descripción=input("Ingrese la descripción:")
        precio=float(input("Ingrese el precio:"))
        stock=int(input("Ingrese el stock actual:"))
        productos[código]=(descripción,precio,stock)
        continua=input("¿Desea cargar otro producto?[n/s]")
    return productos


def imprimir(productos):
    print("Listado completo de productos")
    for código in productos:
        print(código,productos[código][0],productos[código][1],productos[código][2])


def consulta(productos):
    código=int(input("Ingrese el código de artículo a consultar:"))
    if código in productos:
        print(productos[código][0],productos[código][1],productos[código][2])


def listado_stock_cero(productos):
    print("Listado de artículos con stock en cero:")
    for código in productos:
        if productos[código][2]==0:
            print(código,producto[código][0],productos[código][1],productos[código][2])


# bloque principal

productos=cargar()
imprimir(productos)
consulta(productos)
listado_stock_cero(productos)

