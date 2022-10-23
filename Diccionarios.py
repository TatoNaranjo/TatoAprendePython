### Diccionarios ###
"""
Tipo de Estructura en el que podemos Almacenar Datos
de Clave:Valor.

Relación Clave-Valor: Como se define una clave y se le
Asocia un valor.
"""
#Como Crear un Diccionario

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

print("----------//----------")
#Qué lo hace diferente a un set?

my_other_dict = {"Nombre":"Tato","Apellido":"Naranjo","Edad":18,1:"Jose"}

my_dict ={"Nombre":"Tato",
          "Apellido":"Naranjo",
          "Edad":18,
          "Parientes":{"Jose","La jenny", "Alberto"},
          1:1.55
          }

print(my_other_dict)
print(my_dict)
print(len(my_other_dict))
print(len(my_dict))

print("----------//----------")

#Como Acceder a un elemento del diccionario?
print(my_dict["Nombre"])

print("----------//----------")

#Reescribir el valor de la Clave.
my_dict["Nombre"]="Pedro"
print(my_dict["Nombre"])

print("----------//----------")

#Agregar un Campo nuevo al Diccionario
my_dict["Calle"]="Bordeau"
print(my_dict)

print("----------//----------")

#Manera de eliminar un elemento en el Diccionario.
del my_dict["Calle"]
print(my_dict)

print("----------//----------")

#Buscamos si existe la clave dentro del elemento.
#En Realidad no buscamos el valor.
print("Nombre"in my_dict)
print("Tato"in my_dict)#Realmente no lo va a encontrar, es un  valor.

print("----------//----------")

print(my_dict.items()) #Nos muestra Una lista de Clave y Valor

print(my_dict.keys())#Nos muestra un listado de las claves.
print(my_dict.values())#Nos muestra un listado de los valores.

print("----------//----------")

#Creamos un Diccionario Nuevo pero sin valores.
my_list = ["Nombre",1,"Piso"]
my_new_dict = dict.fromkeys((my_list))

my_new_dict =dict.fromkeys(("Nombre",1,"Piso"))
print(my_new_dict)
print("----------//----------")

#Reutilizar Claves de un Diccionario para crear un Diccionario Nuevo
my_new_dict = dict.fromkeys(my_dict)
print((my_new_dict))

print("----------//----------")

#Mete a todas las claves el valor que le estemos Pasando.
my_new_dict = dict.fromkeys(my_dict,("Tato","Naranjo"))
print(my_new_dict)

print("----------//----------")

#Transformarlo a diferentes Listas solo nos retornará las Claves
print(list(my_new_dict.values()))#Retorna los valores, en una Lista de Valores
print(list(my_new_dict))
print(tuple(my_new_dict))
print(set(my_new_dict))