"""
Dada la hoja de puntaje de los participantes para su Día del Deporte Universitario, debe encontrar el puntaje del subcampeón.
te dan puntuaciones. Guárdalos en una lista y encuentra la puntuación del subcampeón.

Input Format: La primera Linea Contiene el numero n de Puntajes. La segunda linea contiene un Arreglo A de Enteros Separados
              Por un espacio.
Output Format: Imprime el Puntaje del SubCampeón

Ejemplo:

Input:
5
2 3 6 6 5

Output:
5

Porque el Segundo Puntaje Más alto es 5

"""

n = int(input())
#Hacemos un mapa del Input que nos dan, asegurandonos de que solo habrán Enteros Ponemos Int
arr = map(int, input().split())
#Declaramos la lista para luego ponerla en un Set, Garantizando que no se repetirán Numeros, y Organizamos La Lista
arr = list(sorted(set(sorted(arr))))

#Imprimimos el segundo Numero más Grande.
print (arr[-2])
