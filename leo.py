'''
Ejercicio
Escribir programa que genere y muestre 
por pantalla un DataFrame con 
los datos de la tabla siguiente:

Mes	Ventas	Gastos
Enero	30500	22000
Febrero	35600	23400
Marzo	28300	18100
Abril	33900	20700
'''

import pandas as pd
datos={'Mes':["Enero","Febrero","Marzo","Abril"],
       "Ventas":[30500,35600,28300,33900],
       "Gastos":[22000,23400,18100,20700]}
contabilidad= pd.DataFrame(datos)
print(contabilidad)


'''
Escribir un programa que permita gestionar 
la base de datos de clientes de una empresa. 
Los clientes se guardarán en un diccionario 
en el que la clave de cada cliente será su NIF,
y el valor será otro diccionario con los datos
del cliente (nombre, dirección, teléfono, 
correo, preferente), donde preferente tendrá el 
valor True si se trata de un cliente preferente.
El programa debe preguntar al usuario por una
opción del siguiente menú: (1) Añadir cliente, 
(2) Eliminar cliente, (3) Mostrar cliente,
(4) Listar todos los clientes, (5) Listar 
clientes preferentes, 
(6) Terminar. En función de la opción elegida 
el programa tendrá que hacer lo siguiente:

Preguntar los datos del cliente, crear un diccionario 
con los datos y añadirlo a la base de datos.

Preguntar por el NIF del cliente y eliminar sus datos 
de la base de datos.

Preguntar por el NIF del cliente y mostrar sus datos.

Mostrar lista de todos los clientes de la base datos 
con su NIF y nombre.

Mostrar la lista de clientes preferentes de la base 
de datos con su NIF y nombre.

Terminar el programa.
'''
clientes={}
opcion=''
while opcion!='6':
    if opcion=='1':
        nif= input("Por favor ingresa el nif del cliente: ")
        nombre= input("Por favor ingresa el nombre del cliente: ")
        direccion= input("Por favor ingresa la dirección del cliente: ")
        teléfono= input("Por favor ingresa el teléfono del cliente: ")
        correo= input("Por favor ingresa el teléfono del cliente: ") 
        preferente=  input("¿Es un cliente preferente? (S/N):  ")
        cliente = {'nombre':nombre, 'dirección':direccion, 'teléfono':teléfono, 'email':correo, 'preferente':preferente=='S'}
        clientes[nif]= cliente
    if opcion=='2':
        nif= input("Intruduce el NIF del cliente: ")
        if nif in clientes:
            del clientes[nif]
        else:
            print("El cliente con el nif ", nif, " no existe ")
            