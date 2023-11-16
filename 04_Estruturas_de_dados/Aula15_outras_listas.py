

#Usando SET

lista1 = [10, 20, 60, 70, 120, 140, 150, 180]

lista2 = [10, 20, 30, 40, 50, 60, 70, 80]

num1 = set(lista1)
num2 = set(lista2)


print(num1 | num2) # "Union" junta as duas e retira os repetidos só deixando um deles
print(num1 - num2) # "diference" Retira totalmente os repetidos só deixando os diferentes
print(num1 ^ num2) # "symetric diference" retira todos os duplicados nas duas listas
print(num1 & num2) # "AND" só mostra os que são repetidos

