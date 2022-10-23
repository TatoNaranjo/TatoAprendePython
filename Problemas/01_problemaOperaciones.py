
print("BIENVENIDO USUARIO")


desicion = int(input("Qué deseas hacer?\n1.Sumar Numeros\n2.Restar Numeros\n3.Multiplicar Numeros\n"))

if desicion == 1:
    cantidadNumeros = input("Ingrese la cantidad de Numeros a Sumar: ")
    numeroIngresado = input("Ingrese Los Numeros: ")
    vectorNum = numeroIngresado.split()
    suma = int(0)
    for x in vectorNum:
        suma = suma+int(x)

    print("La Suma de Tus numeros es:", suma)

if desicion == 2:
    cantidadNumeros = input("Ingrese la cantidad de Numeros a Restar: ")
    numeroIngresado = input("Ingrese Los Numeros: ")
    vectorNum = numeroIngresado.split()
    resta = int(0)
    vectorNum.sort()
    for x in vectorNum:
       resta = x-resta

    print("La Resta de Tus Numeros Es:",resta)

if desicion == 3:
    cantidadNumeros = input("Ingrese la cantidad de Numeros a Operar: ")
    numeroIngresado = input("Ingrese Los Numeros: ")
    vectorNum = numeroIngresado.split()
    multi = int(1)
    for x in vectorNum:
        multi *= int(x)

    print("El Resultado de la Multiplicación de tus Numeros es:",multi)




