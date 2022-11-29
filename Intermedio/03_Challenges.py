"""
EL FAMOSO "FIZZ BUZZ”:
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""

def fizzBuzz():
    increment = 0
    while increment<100:
        increment+=1
        if increment%3 == 0 and increment%5 == 0:
            print("fizzbuzz")
        elif increment % 3 == 0:
            print("fizz")
        elif increment % 5 == 0:
            print("buzz")
        else:
            print(increment)
    return 0

fizzBuzz()

"""
¿ES UN ANAGRAMA?
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
  las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""

def anagramas(word1,word2):
  proof = ""
  if word1.lower() == word2.lower():
      proof = "No Son Anagramas"
  elif sorted(word1.lower()) == sorted(word2.lower()) :
      proof = "Son Anagramas"
  else:
      proof = "No Son Anagramas"
  return proof

print(anagramas("Jose","Jose"))

"""
LA SUCESIÓN DE FIBONACCI
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en
  la que el siguiente siempre es la suma de los dos anteriores.
  0, 1, 1, 2, 3, 5, 8, 13...
"""

def fibonacci():
    anterior = 0
    siguiente = 1

    for index in range(0,50):
        print(anterior)
        fib = anterior+siguiente
        anterior = siguiente
        siguiente = fib

fibonacci()

print("...........//..........")
"""
¿ES UN NÚMERO PRIMO?
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
"""

def primeNumber():
    for sucesion in range (1,101):
        if sucesion >= 2:
            divisible = False
            for i in range(2,sucesion):
                if(sucesion % i==0):
                    divisible = True
                    break

            if not divisible:
                print(sucesion)

primeNumber()

"""
INVIRTIENDO CADENAS
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""

def reverse(word):
    reversedword = ""
    lista = list(word)
    tamaño = len(word)
    for x in range (1,tamaño+1):
        reversedword+=lista[-x]
    return reversedword

print(reverse("Alicia Sierra"))