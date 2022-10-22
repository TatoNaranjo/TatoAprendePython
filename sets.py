### Sets ###
"""
Parecen Una lista, pero tiene Unas Cuantas
Diferencias
"""


#Creando un Set
my_set = set()
my_other_set ={}
print(type(my_set))
print(type(my_other_set))# Inicialmente es un Diccionario
print("----------//----------")


my_other_set={"Tato","Naranjo",35}
print(type(my_other_set))

print("El Tamaño es:",len(my_other_set))
#print(my_other_set[1]) #No deja Llamar a posiciones para Imprimir

#Un Set no es una Estructura Ordenada
my_other_set.add("ElTatoNaranjo")
print(my_other_set)
print("----------//-----------")

#Un Set No admite Elementos Repetidos
my_other_set.add("ElTatoNaranjo")
print(my_other_set)
print("----------//-----------")

#Sintaxis para comprobar si existe el Elemento en el Set
print("Tato" in my_other_set)
print("Tatx" in my_other_set)

print("----------//-----------")

#Como eliminar un elemento de la Lista
my_other_set.remove("Tato")
print(my_other_set)
print("----------//-----------")

#Limpiando Completamente el Set
my_other_set.clear()
print(my_other_set)
print("El Tamaño del Set es:",len(my_other_set))

print("----------//-----------")

#Hemos Eliminado completamente la variable
#del my_other_set
#print(my_other_set)

print("----------//-----------")

#Creando una Lista a Partir de un Set para acceder a una
#Posicion.
my_set = {"Tato","Naranjo", 45}
my_list = list(my_set)
print(my_list)
print(my_list[2])

print("----------//-----------")
#Unir Listas y Sets

my_other_set = {"Java","Go","Python"}
my_new_set = my_set.union(my_other_set)
print(my_new_set)

#No se unirá a si mismo ya que es un Set Duplicado

#RECUERDA: No Acepta Repetidos.
print(my_new_set.union(my_new_set))

#Hallando la diferencia entre my new Set y Set.
print(my_new_set.difference(my_set))
