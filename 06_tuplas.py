## Tuplas ##
"""
¿Qué es Una Tupla?
Parece una Lista, pero...

Primera Diferencia: Los Metodos funcionan Diferentes en
las tuplas y las Listas.

Segunda Diferencia: Las tuplas no admiten cambios en las
Variables. Las tuplas son variables Constantes.

"""

#Definiendo Tuplas
my_tuple = tuple()
my_other_tuple=()

my_tuple = (35,1.72,"Tato","Naranjo")
print(my_tuple)
print(type(my_tuple))
print("----------//----------")

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) IndexError
#print(my_tuple[-6]) IndexError
print("----------//----------")
#Para contar cuantos elementos hay en una Tupla

print(my_tuple.count("Tato"))

#Nos devuelve el indice en el que se encuetre el Primer Elemento
print(my_tuple.index("Naranjo"))

#Se toteará porque  una Tupla no admite sobre Escribir Variables.
#Una Tupla es Inmutable
#my_tuple[1] = 1.75
#print(my_tuple)

#Se pueden Concatenar Tuplas
print(my_tuple+my_other_tuple)

my_sum_tuple = my_tuple+my_other_tuple
print(my_sum_tuple)

print("----------//----------")

#Imprimimos los Elementos entre el 3 y el 6
#Es decir, imprimimos Elementos Concretos.

print(my_tuple[3:6])
print("----------//----------")


"""
Cuando Trabajemos con datos, si son Inmutables, Mejor.
"""
#En Caso de querer cambiar de Tuplas a Listas.
my_tuple=list(my_tuple)
print(type(my_tuple))
print("----------//----------")
my_tuple[2] = "TatoNaranjo"
my_tuple.insert(1,"Jose")
print(my_tuple)

#Volviendo a pasar de Listas a Tuplas
my_tuple = tuple(my_tuple)
print(type(my_tuple))

#Irónicamente, ahora borramos totalmente la variable.
#Ya no Está definida y por eso totearía y mostraría Error
# del my_tuple
# print(my_tuple)