## Ciclos Repetitivos ###
"""
Mecanismo que sirve para Iterar.
Iterar: Intentar repetir algo.
Es decir, usamos los Loops para pasar Más de una vez
por el Código.
"""

#While
my_condition = 1

while my_condition <=10:
    print(my_condition)
    my_condition+=1

print("----------//----------")
#While con Ifs anidados.
my_condition = 0
while my_condition<20:
    my_condition+=1
    if my_condition==15:
        print("Mi Numero es 15")
        print("Se Detiene la Ejecución.")
        #El break detiene la ejecución del Codigo.
        break
    else:
        print(my_condition)
print("La Ejecución Continua")

print("----------//----------")

# FOR
"""
Sirve para iterar un estado de elementos.
"""
my_list = [35,24,62,52,30,30,17]

for element in my_list:
    print(element)

print("----------//----------")
#Imprimiendo un Diccionario
my_dict ={"Nombre":"Tato",
          "Apellido":"Naranjo",
          "Edad":18,
          "Parientes":{"Jose","La jenny", "Alberto"},
          1:1.55
          }
for element in my_dict:
    print(element) #Imprime solo las Claves/Keys.
print("----------//----------")
for element in my_dict:
    print(element)
    if element == "Edad":
        break
else:
    print("El Bucle for para Diccionario Ha Finalizado")

