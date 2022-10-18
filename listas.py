### Listas ###
"""
Una lista nos proporciona Operaciones de Listas,
Por lo que no se puede considerar un Array.

Lista: Super Conjunto de un Arreglo

Un Array es más Inamovible

"""

#Como declarar Listas
my_list =list()
my_other_list=[]
print("----------//----------")
#Viendo la longitud de la Lista
print(len(my_list))

my_list=[34,24,62,52,30,30,17]
print(my_list)
print(len(my_list))
print("----------//----------")
#Se puede llenar con Cualquier tipo de Dato
my_other_list=[35,1.22,"Tato","Naranjo"]
print(type(my_other_list))
print(my_other_list)
print("----------//----------")
#Imprimiendo Posiciones // Determinando Posiciones

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
#print(my_other_list[4])IndexError
#print(my_other_list[-5])IndexError
print("----------//----------")
#Cuenta cuantos elementos con este nombre Se Encuentran en la Lista
print(my_other_list.count("Tato"))

#Asignando Variables a cada Elemento de la Lista.
age,height,name,surname = my_other_list
print(name)

#Concatenando Listas
print(my_list+my_other_list)
print("----------//----------")
#Uniendo un nuevo elemento a la Lista.
my_other_list.append("TatoNaranjo")
print(my_other_list)

#Insertar un Elemento en una Posición Específica a la lista
my_other_list.insert(1,"Olakhease")
print(my_other_list)

#Eliminar Un Elemento específico de la lista
my_list.remove(30)
print(my_list)

#Elimina el ultimo Elemento, Pero por si lo necesitamos nos
#Devuelve el valor Eliminado
my_list.pop()

print(my_list)
print(my_list.pop())

#Especificando el Index del Pop
myPopElement = my_list.pop(2)
print(myPopElement)

#Eliminar un elemento de la Lista por medio de un Index
del my_list[2]
print(my_list)

#Eliminar Un Elemento específico de la lista
my_other_list.remove("Olakhease")
print(my_other_list)

"""
Remove: Elimina el elemento que sabemos que está dentro, El Primero que Encuentra
Del:    Elimina por Índice
"""
print("----------//----------")

#SobreEscribinendo Elementos en una Posición Específica


my_other_list[1] = "Azul"
print(my_other_list)

#Genera una "Copia de Seguridad" de la lista.
my_new_list = my_list.copy()
print(my_new_list)

#Voltear una Lista
my_new_list.reverse()
print(my_new_list)

#Organizar una Lista

my_new_list.sort()
print(my_new_list)


