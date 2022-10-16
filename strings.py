### Strings ###

myString = "Mi String"
myOtherString = 'Mi otro String'
print("-----//-----")
#Determinando Longitudes de Strings
print(len(myString))
print(len(myOtherString))
print("-----//-----")
#Concatenar Strings
print(myString+" "+myOtherString)

#Caracteres especiales con Strings

print("-----//-----")
nuevoString="Este es un String \ncon Salto de Linea"
print(nuevoString)

tabString="\tEste es un String con Tabulacion"
print(tabString)

scapeString="\tEste es un String \n escapado"
print(scapeString)
print("-----//-----")

# Formateo
name,surname,edad= "Tato","Naranjo",18

print("Mi nombre es {} {} y mi edad es {} años".format(name,surname,edad) )
print("Mi nombre es %s %s y mi edad es %s años" %(name,surname,edad)) #Se usa %s si Trabajamos con el Numero Formateado


"""
MALA PRÁCTICA
print("Mi nombre es" + name + " "+surname+ "y mi edad es"+ str(edad)+ " años")

"""
#Inferencia de Datos

#Se Imprime Literal
print("Mi nombre es {name} {surname} y mi edad es {edad} años")
#Pero..
print(f"Mi nombre es {name} {surname} y mi edad es {edad} años")
print("-----//-----")
# Desempaquetado de Variables
language = "Python"
a,b,c,d,e,f = language
print(a)
print(b)
"""
Marca error porque no hay suficientes variables para
desempaquetar los Chars
language = "Python"
a,b = language
print(a)
print(b)

"""
print("-----//-----")
#División de caracteres

language_slice = language[1:3]
print(language_slice)
language_slice = language[1:]
print(language_slice)
language_slice = language[0:6:2]
print(language_slice)

#Reversion de Caracteres
print("-----//-----")
reversed_language = language[::-1]
print(reversed_language)

# Funciones del Sistema
print("-----//-----")
print(len(language)) #Longitud del String
print(language.capitalize()) #Pone la primer Palabra en Mayuscula
print(language.upper())#Pone el String en Mayusculas
print(language.count("t"))#Cuantos Caracteres tiene
print(language.isnumeric())#Nos dice si es un Numero: False
print("1".isnumeric())#Nos dice si es un Numero: True
print(language.lower())#Pone el String en Minusculas
print(language.upper().isupper())#Primero Pasa a mayusculas y luego comprueba si Es mayúscula
print(language.startswith("Py"))#Nos indica si el String comienza o no con las Letras





