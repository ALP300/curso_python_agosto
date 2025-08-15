'''
1. Determina el mayor de tres números: 
Declara tres variables a, b y c con valores numéricos 
y utiliza condicionales  para determinar cuál de ellos
es el mayor. 
'''


a= 25
b= 20
c= 30
if a>=b and a>=c:
    mayor= a
elif b>=a and b>=c:
    mayor= b
else:
    mayor=c

print("El mayor valor es:  "+str(mayor))
print(f"El mayor valor es:  {mayor}")
print("El mayor valor es:  ", mayor)

