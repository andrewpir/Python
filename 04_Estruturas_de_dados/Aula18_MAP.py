

# https://docs.python.org/3/library/functions.html

#aplica uma função a um iterable(list, tuple, dic, etc)


lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def multi(x):
    return x * 2


    
    
lista2 = map(multi, lista1)

print(list(lista2))  #precisa ser convertido em lista pois ele sai em forma de objeto


# com Lambda

#lista3 = map(lambda x: x * 2, lista1)

print(list(map(lambda x: x * 2, lista1)))






