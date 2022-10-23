### Funciones ###

# Como definir una Función(Metodo) en Python
def my_function():
    print("Esto es Una función")
my_function()
my_function()
"""
COMENTADO PORQUE LO HICE YO PROBANDO XDXD
#Creando una funcion que pide datos y retorna Algo.
def my_return_function(x,y):
    suma = x+y
    return suma
x = int(input())
y = int(input())
print(my_return_function(x,y))
"""
print("----------//----------")

#Creando una funcion que pide 2 numeros y los suma
#Funcion que pide Parametros:
def sum_two_values(primer_numero,segundo_numero):
    print(primer_numero+segundo_numero)

sum_two_values(2,3)

print("----------//----------")

#Funcion que retorna parámetros.
def sum_two_values_with_return(primer_numero,segundo_numero):
    return(primer_numero+segundo_numero)

my_result = sum_two_values_with_return(2,4)
print(my_result)

print("----------//----------")
#Rectificar posición de Llegada
def print_name (name,surname):
    print(f"{name} {surname}")

print_name(surname="Naranjo",name="Tato")
print("----------//----------")

#Dando un valor Por Defecto a un parámetro.
def print_name_with_default (name,surname,alias = "Sin Alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Tato","Naranjo") #Ejemplo Sin Alias
print_name_with_default("Tato","Naranjo","ElTato")

print("----------//----------")
#Pasando muchos datos a un solo Parámetro.
#Numero de Parámetro Dinamico con *

def print_texts(*texts):
    for text in texts:
        print(text)

print_texts("Tato","El Velocista","Naranjo")