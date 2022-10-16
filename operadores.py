
#Operaciones con Numeros

#Suma
print(3+4)
#Resta
print(3-4)
#Multiplicacion
print(3*4)
#Division
print(3/4)
#Modulo
print(10%3)
#Division Aproximada
print(10//3)
#Potencia
print(2**3)
print("----------//---------")
#Operaciones con Strings

print("Hola "+"Python") #Concatenando Strings

#Posibles Errores.
"""
Print("Hola"-"Python") 
Esto totearía el código xd

print ("Hola"+5)
No se puede mezclar un String con un Int
"""
#Fin de los Posibles errores xd
print("Hola "+str(5)) # Esto si funciona porque pasamos el 5 a string

print("Hola "*5)# Hola se Multiplica 5 veces, es decir se imprime 5 veces

#Convirtiendo Floats a ints para multiplicar Strings
my_float = 2.5*2
print("Hola "*int(my_float))

### Operadores Comparativos ###
print("----------//---------")
# Comparando Numeros
print(3>4)
print(3<4)
print(3<=4)
print(3>=4)
print(3==4)
print(3!=4)

print("----------//---------")
#Comparando Strings
print("Hola">"Python")
print("Hola"<"Python")
print("Hola">="Python")
print("Hola"<="Python")
print("Hola"=="Python")
print("Hola"!="Python")
print("----------//---------")

print("aaaa">= "abaa")# Ordenacion Alfabetica por ASCII
print(len("Hola")>= len("palo")) # Cuenta Caracteres
print("----------//---------")

### Operadores Lógicos ###
print(3>4 and "Hola">"Python") # Y
print(3>4 or "Hola">"Python") # O

print (3<4 and "Hola"<"Python")#Verdadero & Verdadero
print(3<4 or "Hola"<"Python")#Verdadero O Verdadero

print(3<4 or ("Hola"<"Python" and 4==4))

print(not(3>4)) # Negación




