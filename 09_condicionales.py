### Condicionales ##
"""
Representan la manera de establecer flujos de Ejecución
en Nuestro Codigo. Es decir si una Acción Se Ejecuta o No.
 Si La acción está tabulada, entonces está dentro del Condicional.
"""

my_condition = False

if my_condition: #Lo Mismo que if my_condition == True:
    print("Se Ejecuta la Condición del If")

print("La Ejecución Continua")

print("----------//----------")
my_condition = 5*2

if my_condition == 10:
    print("Se Ejecuta la Condición del Segundo If")


if my_condition < 10:
    print("Se Ejecuta la Condición del Tercer If")

print("----------//----------")

#USO DE IF Y ELSE
if my_condition == 10:
        print("Es Igual a 10")
else:
        print("Es Diferente de 10")

print("----------//----------")

#USO DEL IF Y ELSE PERO CON AND
my_condition=5*5

if my_condition > 10 and my_condition <20:
     print("Es Mayor a 10 y Menor que 20")
else:
    print("Es Menor que 10 o Mayor a 20")

print("----------//----------")

#USO DEL ELIF
"""
Orden de Jerarquías: If, Elif, Else
"""

my_condition= 1


if my_condition > 10 and my_condition <20:
     print("Es Mayor a 10 y Menor que 20")
elif my_condition == 1:
     print("Es Igual a Uno")
else:
    print("Es Menor que 10 o Mayor a 20")

print("----------//----------")

my_string = "Mi Cadena de Texto"

if my_string:
    print("Mi Cadena de texto no es Vacía")

if my_string == "Mi Cadena de Textoooo":
    print("Las Cadenas de Texto Coinciden :D")

print("----------//----------")
#Negando el Elemento. Si Mi cadena NO Está Vacía
if not my_string:
    print("Mi Cadena de texto no es Vacía")




