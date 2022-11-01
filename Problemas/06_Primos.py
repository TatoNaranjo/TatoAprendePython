contador = 1

while contador<=100:
    divisible = 0
    x = 1
    while x<=contador:
        if(contador%x==0):
            divisible+=1
        x += 1
    if divisible==2:
        print(contador," es un Numero Primo")
    else:
        print(contador,"No Es un Numero Primo")


    contador+=1

