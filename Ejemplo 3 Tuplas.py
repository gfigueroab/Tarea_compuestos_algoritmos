#Almacenar en una lista de cinco elementos las tuplas con el nombre del empleado
#Implementar las funciones:
#1) Carga de empleados.
#2) Impresión de los empleados y sus sueldos.
#3) Nombre del empleado con sueldo mayor.
#4) Cantidad de empleados con sueldo mayor a 1000.

def carga():
    empleados=[]
    for x in range(5):
        nombre=input("Nombre del empleador:")
        sueldo=int(input("Ingrese el sueldo:"))
        empleados.append((nombre,sueldo))
    return empleados


def imprimir(empleados):
    print("Listado de los nombres de empleados y sus sueldos")
    for nombre,sueldo in empleados:
        print (nombre, sueldo)


def mayor_sueldo(empleados):
    empleado=empleados[0]
    for emp in empleados:
        if emp[1]>empleado[1]:
            empleado=emp
    print("Empleado con mayor sueldo:",empleado[0],"su sueldo es",empleado[1])


def sueldo_menor1000(empleados):
    cant=0
    for empleado in empleados:
        if empleado[1]<1000:
            cant=cant+1
    print("Cantidad de empleados con un sueldo menor a 1000 son:",cant)


# bloque principal

empleados=carga()
imprimir(empleados)
mayor_sueldo(empleados)
sueldo_menor1000(empleados)
