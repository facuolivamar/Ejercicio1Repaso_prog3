#2) ES BISIESTO??
#Escriba un programa que pregunte un año y que escriba si es bisiesto o no.
#Se debe pasar por parámetro el año a una función.
#Se recuerda que los años bisiestos son múltiplos de 4, pero los múltiplos de 100 no lo son, aunque los
#múltiplos de 400 sí.
#Estos son algunos ejemplos de posibles respuestas: 2012 es bisiesto, 2010 no es bisiesto, 2000 es bisiesto,
#1900 no es bisiesto.


lista = [2012,2010,2000, 1900]
for i in lista:
    if (i%4) == 0 and (i%100) != 0:
        print('anio bisiesto: {}'.format(i))
    else:
        print('anio no bisiesto: {}'.format(i))

