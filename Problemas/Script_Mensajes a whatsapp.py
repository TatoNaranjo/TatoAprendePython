# Importamos el ModuMódulo
#
import pywhatkit
# Usamos Un try-except
try:
  # Enviamos el mensaje
  pywhatkit.sendwhatmsg("+57**********",
                        "Hola Daniel, este es un mensaje mandado por un Bot de Python",
                        7,18)
  print("Mensaje Enviado")
  
except:
  print("Ocurrio Un Error")