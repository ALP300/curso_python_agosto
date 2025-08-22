'''
Escribir un programa que permita gestionar la base de datos de 
clientes de una empresa. Los clientes se guardarán en un 
diccionario en el que la clave de cada cliente será su NIF,
y el valor será otro diccionario con los datos del cliente 
(nombre, dirección, teléfono, correo, preferente), 
donde preferente tendrá el valor True si se trata de un 
cliente preferente. El programa debe preguntar al usuario 
por una opción del siguiente menú: (1) Añadir cliente,
(2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, 
(5) Listar clientes preferentes, (6) Terminar. En función de 
la opción elegida el programa tendrá que hacer lo siguiente:

Preguntar los datos del cliente, crear un diccionario con los datos 
y añadirlo a la base de datos.

Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.

Preguntar por el NIF del cliente y mostrar sus datos.

Mostrar lista de todos los clientes de la base datos con su NIF y nombre.

Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.

Terminar el programa.
'''
clientes={}
opcion=''
while opcion!='6':
    print("""
    Menú de opciones:
    1. Añadir cliente
    2. Eliminar cliente
    3. Mostrar cliente
    4. Listar todos los clientes
    5. Listar clientes preferentes
    6. Terminar
    """)
    opcion = input("Selecciona una opción: ")
    if opcion=='1':
        nif= input("Por favor, ingresa el nif del cliente: ")
        nombre= input("Por favor, ingresa el nombre del cliente: ")
        direccion= input("Por favor, ingresa la dirección del cliente: ")
        telefono= input("Por favor, ingresa el teléfono del cliente: ")
        correo= input("Por favor, ingresa el correo del cliente: ")
        preferente=input("¿Es cliente preferente (S/N):  ")
        cliente= {'Nombre':nombre,'Direccion':direccion,"Telefono": telefono, "Correo": correo, 'preferente': preferente=='S'}
        clientes[nif]=cliente
    
    if opcion=='2':
        nif= input("Por favor, ingresa el NIF del cliente a eliminar: ")
        if nif in clientes:
            del clientes[nif]
            print(f"Cliente con NIF {nif} eliminado.")
        else:
            print("Cliente no encontrado.")
    
    if opcion=='3':
        nif= input("Por favor, ingresa el NIF del cliente a mostrar: ")
        if nif in clientes:
           print('Nif: ', nif)
           for key, value in clientes[nif].items():
               print(f"{key}: {value}")          
        else:
            print("Cliente no encontrado.")

    if opcion=='4':
        print("Lista de todos los clientes:")
        for nif, datos in clientes.items():
            print(f"NIF: {nif}, Nombre: {datos["Nombre"]}")
            
    if opcion=='5':
        print("Lista de clientes preferentes:")
        for nif, datos in clientes.items():
            if datos['preferente']:
                print(f"NIF: {nif}, Nombre: {datos['Nombre']}")