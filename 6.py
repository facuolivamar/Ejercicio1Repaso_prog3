#6) A CONTAR VOCALES!
#Escribir una función que reciba como parámetro una frase y devuelva la cantidad de vocales que ésta tiene.

consonantesyvocales = 'abcdefgdsasdsdseiueouroesdsad'
x = 0
print(consonantesyvocales)
for i in consonantesyvocales:
    if i.lower() == 'a' or i.lower() == 'e' or i.lower() == 'i' or i.lower() == 'o' or i.lower() == 'u':
        x = x+1
print('cantidad de vocales: {}'.format(x))