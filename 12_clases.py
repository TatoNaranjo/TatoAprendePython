### Clases ###
"""
Como definir una clase?

Pass: Evita que la Clase Persona colapse si no tiene una
Acción. Es una forma de Intentar que la Clase se Ejecute
SE USA CUANDO LA CLASE NO TIENE NADA


"""

class MyEmptyPerson:
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())
print("----------//..........")
class Person:
    """
    El Def Init nos sirve para crear un Constructor de
    La Clase.Un Lugar donde podemos crear atributos relacionados
    a la persona.

    """


    def __init__(self, name, surname, alias = "No Alias"):
        self._name = name #propiedad Protegida
        self.surname = surname
        self.full_name = f"{name} {surname} {alias}"

    def walk(self):
        print(f"{self.full_name} Está Caminando")

    def get_name(self):
        return self._name

    """ 
      #La Forma de Llamar a un parametro de la Clase es Self
       #Si pongo self puedo acceder a lo guardado dentro de la Clase
    """
#CREANDO UN CONSTRUCTOR SOBRECARGADO
my_Person = Person("Tato","Naranjo")
print(my_Person.name)

print(my_Person.full_name)


my_other_person = Person("Tato","Naranjo","TatoNaranjo")
print(my_other_person.full_name)

my_other_person.walk()

print("----------//----------")

#SobreEscribiendo una variable

my_other_person.full_name= "Hola, Cambié La variable xdxd"
my_other_person.walk()