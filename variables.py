#Aprendiendo Variables
from pip._vendor.pyparsing import nums

#Este es un numero Entero
entero = 5
print("Este es un numero Entero:",entero)
#Este es un numero Decimal
decimal = 5.5
print("Este es un Numero Decimal: ",decimal)
#Este es un Numero Imaginario
imaginario = 5j
print("Este es un Numero Decimal: ",imaginario)
#Este es un Texto Escrito con Comillas Dobles
texto = "Este es un Texto"
print("Este es un Texto Normal: ",texto)
#Este es un Texto Escrito con Comillas Simples
textoComillas = 'Este es un Texto con Comillas Simples'
print("Este es un Texto con Comillas Simples",textoComillas)

negativo = -54
print(abs(negativo))

print("Hola Amiguito, Digita tu numero Por Favor :D")
numeroUsuario = input()
print("Tu numero es: ",numeroUsuario," verdad?")