#5) PALINDROMOS
#Escribir una función que reciba como parámetro una palabra, y devuelva True si esa palabra es un
#palíndromo y False si no lo es.
#Ejemplo:
#esCapicua("neuquen") === True
#esCapicua("jovenes") === False
def capicua(palabra, palabra_capicua):
    for i in palabra:
        palabra_capicua = i + palabra_capicua
    if palabra == palabra_capicua:
        print('True')
        return True
    else:
        print('False')
        return False


palabra = "neuquen"
palabra2 = "jovenes"

palabra_capicua = ''
palabra2_capicua = ''

capicua(palabra, palabra_capicua)
capicua(palabra2, palabra2_capicua)

print(palabra2_capicua)