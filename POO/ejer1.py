#PERRO
    #NOMBRE
    #RAZA
    #EDAD
    #PESO
    
#CLIENTES
    # NOMBRE
    # CORREO
    # TELEFONO
    # CONTRASEÑA
    # DIRECCION
    
#TRABAJADORES
    #NOMBRE
    #CORREO
    #TELEFONO
    #CONTRASEÑA
    #DIRECCION
    #PUESTO
    #FECHA CONTRATACION
    #SALARIO
    
#PRODUCTOS
    #NOMBRE
    #DESCRIPCION
    #PRECIO
    #STOCK
    #CATEGORIA
    
#VENTAS
    #FECHA
    #CLIENTE
    #TRABAJADOR
    #PRODUCTOS
    #TOTAL
    
#INGREDIENTES
#MESAS
#PEDIDOS
#FACTURAS
#REPARTIDORES



class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre}")
     

persona1= Persona("Pepe")
print(persona1.saludar())