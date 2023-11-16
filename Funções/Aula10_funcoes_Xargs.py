
#função com indefinidos argumentos


'''
def soma(*numeros):
    resultado = 0
    for i in numeros:
        resultado += i
        
    return resultado

x = soma(8,8,8,8,8,8,8)

print(x)

'''

#Função com Xargs com mistura
'''
def agencia(**carro): #isso forma um dicionário com x entradas e x parametros
    return carro


print(agencia(marca = "Gol",cor = "Branco",motor = 1.0, placa = 1234))

'''

#Módulos e importações

#numero fatorial de 4
# 4*3*2*1

import math #importar o modulo, verificar o nome dos modulos pela internet (python module)

print(math.factorial(4))

print(math.floor(2.7))

print(math.ceil(2.7))
