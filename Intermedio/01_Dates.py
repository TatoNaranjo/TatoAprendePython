### Dates ###
"""
Como crear fechas en Python
"""
from datetime import datetime

now = datetime.now()


print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)

timestamp = now.timestamp()
print(timestamp)

#Creación de Fechas
print("----------//----------")



def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.microsecond)
    print(date.timestamp())

print_date(now)

year_2023 = datetime(2023,1,1)
print_date(year_2023)

print("----------//----------")
#Objeto Time: Sirve para encapsular el Tiempo
from datetime import time
#Indicando el tiempo según orden.
current_time = time(22,2,6)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)
print(current_time.microsecond)

#Parte capaz de Agrupar las fechas
from datetime import date
current_date = date(22,2,9)

print(current_date.year)
print(current_date.month)
print(current_date.day)

print("----------//----------")
current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)

print("----------//----------")

#Operaciones con Fechas

current_date = date(current_date.year,current_date.month +1,current_date.day)


diference = year_2023 - now
print(diference)

diference = year_2023.date()-current_date
print(diference)

print(year_2023.time())

#TimeDelta: Sirve para trabajar con diferentes franjas de Fechas
#Sirve para trabajar con valores absolutos.
from datetime import timedelta
time_delta = timedelta()

starts_timeDelta = timedelta(200,100,100,weeks=10)
end_timeDelta = timedelta(300,100,100,weeks=15)

print(end_timeDelta-starts_timeDelta)
print(starts_timeDelta+end_timeDelta)





