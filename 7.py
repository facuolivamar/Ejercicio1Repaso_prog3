#7) NUMEROS STEP!
#Cuando en un número la diferencia entre cada par de dígitos consecutivos es uno, se lo llama número "step"
#(como el 123234, el 9876787654, etc.).
#Escribir una función, que reciba como parámetro un número y devuelva True si es un número step o False si
#no lo es.

numero_step = '1116787654'
i_ant = 0
for i in numero_step:
    if abs(int(i)-int(i_ant)) == 1:
        print('True')
    else:
        print('False')
    print(i)
    i_ant = str(i)