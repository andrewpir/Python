

#forma mais rapida para listas, dic, etc
#valores em Bytes

from sys import getsizeof # importa de sys a possibilidade de ver o quanto gasta de memória



numeros = [x * 10 for x in range(1000)]

print(type(numeros))
#print(numeros)
print(getsizeof(numeros))


print("=======================")


numeros = (x * 10 for x in range(1000))  # com as () vira um generator object

print(type(numeros))
#print(list(numeros))
print(getsizeof(numeros))
