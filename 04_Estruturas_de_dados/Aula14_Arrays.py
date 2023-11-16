


# array (Matriz) 
# https://docs.python.org/3/library/array.html

from array import array

letras = ["a", "b", "c", "d"]

numeros_i = [10, 20, 30, 40]

numeros_f = [1.2, 2.2, 3.2, 4.2]

print(letras)
print(numeros_i)
print(numeros_f)

#é preciso usar uma letra antes para indicar o tipo de array (VER NO SITE) 

letrasa = array("u", ["a", "b", "c", "d"])
numeros_ia = array("i", [10, 20, 30, 40])
numeros_fa = array("f", [1.2, 2.2, 3.2, 4.2])

print(letrasa)
print(numeros_ia)
print(numeros_fa)