#Aprendiendo Variables
from pip._vendor.pyparsing import nums

#Este es un numero Entero

entero = 5
print("Este es un numero Entero:",entero)

#Este es un numero Decimal

decimal = 5.5
print("Este es un Numero Decimal: ",decimal)

#Este es un Numero Complejo

complejo = 5j
print("Este es un Numero complejo:", complejo)

#Este es un Texto Escrito con Comillas Dobles

texto = "Este es un Texto"
print("Este es un Texto Normal:",texto)

#Algunas funciones del Sistema
print("Tiene:",len(texto),"letras")

#Este es un Texto Escrito con Comillas Simples

textoComillas = 'Este es un Texto con Comillas Simples'
print("Este es un Texto con Comillas Simples:",textoComillas)

negativo = -54
print(abs(negativo))

#Variables en una sola linea

nombre,apellido,edad,sexo = "Tato","Naranjo",14,"Masculino"
print("Hey,Soy:",nombre,apellido,"Tengo:",edad,"Años y Mi Sexo Es:",sexo)

#Como solicitar datos por Consola
nombreUsuario = input("Hola Amigo, ¿Como te llamas? ")
edadUsuario = input("¿Qué Edad Tienes? ")

#¿Como imprimir el tipo de dato de una variable?
u = 5

print(type(u))
