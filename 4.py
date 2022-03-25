#4) ORDEN POR FAVOR!
#Realizar una función, que reciba como parámetro una lista compuesta por números enteros y que nos
#devuelva otra lista con el mismo contenido pero ordenada de mayor a menor

lista = [8,10,2,6,5,4,3,2,1]
#lista.sort()
print(lista)
sort_lista = []

for _ in range(len(lista)):
    for i in range(len(lista) - 1):
        if lista[i] < lista[i+1]:
            lista[i], lista[i+1] = lista[i+1], lista[i]
print(lista)
