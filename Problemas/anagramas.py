"""
  Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Bool) según sean o no anagramas.
  Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
  NO hace falta comprobar que ambas palabras existan.
  Dos palabras exactamente iguales no son anagrama.
"""
palabra1 = input()
palabra2 = input()
confirmacion = False
palabra1Organizada = ''.join(sorted(palabra1.lower()))
palabra2Organizada = ''.join(sorted(palabra2.lower()))
if palabra1Organizada==palabra2Organizada:
    confirmacion = True
    print(confirmacion)
else:
    print(confirmacion)



