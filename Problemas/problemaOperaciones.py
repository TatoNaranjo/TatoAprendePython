
print("BIENVENIDO USUARIO")
cantidadNumeros = input("Ingrese la cantidad de Numeros a Operar: ")
numeroIngresado = input("Ingrese Los Numeros: ")
vectorNum = numeroIngresado.split()

desicion = input("Qué deseas hacer con estos numeros?\n1.Sumarlos\n2.Restarlos\n3.Multiplicarlos\n")

if int(desicion) == 1:
    sumatoria = 0
for x in vectorNum:
    sumatoria = int(x)+int(sumatoria)
else:
    print("El resultado de la suma de tus numeros es",sumatoria)

if int(desicion)== 2  :
    resta = 0
for x in vectorNum:
    resta = int(resta)- int(x)
else:
    print("El resultado de la suma de tus numeros es", resta)








