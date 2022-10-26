### Manejo de Errores ###
"""
Si queremos controlar unos errores los ponemos dentro de Try
"""
numberOne, numberTwo = 5,1
numberTwo = "1"

#Error
#Python no puede sumar una cadena de texto con un Numero

#TRY-EXCEPT
try:
    print(numberOne+numberTwo)
    print("No se Ha Producido un Error")
except:
    print("Se Ha producido un Error")
#TRY EXCEPT ELSE
try:
    print(numberOne+numberTwo)
    print("El Programa Funciona")
except:
    print("Se Ha producido un Error")
else: #Opcional: Se ejecuta si no hay excepciones
    print("La ejecución continua perfectamente.")
finally: #Opcional: Se ejecuta Siempre
    print("la Ejecución Continua")
print("----------//----------")
 #Captura de Excepciones por Tipo
try:
    print(numberOne+numberTwo)
    print("No se ha producido ningun error")
except ValueError: #Se Ejecuta SOLO si se produce una Excepcion
    print("Se Ha Producido un ValueError.")
except TypeError:
    print("Se ha producido un TypeError")

print("----------//----------")

#Captura de la Informacion de la Excepción
try:
    print(numberOne+numberTwo)
    print("El Programa Funciona Correctamente")
except ValueError as error:
    print("Se produjo un ValueError")
    print(error)
except TypeError as Error:
    print("Se produjo un TypeError")
    print(Error)
except Exception as Error: #Sea el Error que sea será Controlado
    print("Esto es un Fallo")
    print(Error)

