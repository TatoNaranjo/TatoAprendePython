### Modulos ###

"""
Libreria o lugar donde utilizamos código que tenemos en
Otros Lugares a los que tenemos acceso.
Ej:
"""
#Como Acceder a otros Ficheros?
import module
#Acceder a las funciones.
module.sumValues(2,3,5)
module.multiply(2,3,5)

print("---------//---------")
#Importar unicamente una funcion del Fichero
from module import sumValues, multiply
sumValues(2,3,5)
multiply(2,3,5)

print("---------//---------")

import math

print(math.pi)
from math import pi as PI_VALUE
print(PI_VALUE)