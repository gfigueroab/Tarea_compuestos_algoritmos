#Realizar la carga de valores enteros por teclad,
#almacenarlos en una lista. Finalizar la carga de enteros al ingresar el cero.
#Mostrar finalmente el tamaño de la lista.
Lista=[]
valor=int(input("Ingresar valor (0 para finalizar):"))
while valor!=0:
    Lista.append(valor)
    valor=int(input("Ingresar valor (0 para finalizar):"))

print("Tamaño de la lista:")
print(len(Lista))
