#introdução a funções
'''
def boas_vindas():
    print("Olá Mundo")
    print("estou dentro de uma função")
    print("Um Monte de código")
    
boas_vindas()

boas_vindas()

'''

#função de soma
'''
def somadenumeros():
    numero1 = 10
    numero2 = 5
    resultado = numero1 + numero2
    print(f"O resultado é {resultado}")

def somadenumeros1():
    numero1 = 20
    numero2 = 30
    resultado = numero1 + numero2
    print(f"O resultado é {resultado}")


somadenumeros()

somadenumeros1()


#print(numero1) #isso daria erro pois numero1 e numero 2 são variaveis LOCAIS e funcionam apenas na função

'''

#Parametros e Argumentos
'''
def boasvindas(nome, numero):
    print(f"ola {nome}")
    print(f"um numero é {str(numero)}")


boasvindas("Andrew", 22)
boasvindas("Joao", 31)
boasvindas("Juliano", 24)


# boasvindas("Pirex") da erro se não tiver valores default ou non default
# boasvindas("Pirexs", 24, 28)

def boasvindascomdefault(nome = "comprador", numero = 18): #os que {forem definidos} tem que ser DEPOIS dos não definidos, ou seja, tem que ser por ultimo
    print(f"ola {nome}")
    print(f"um numero é {str(numero)}")


boasvindascomdefault()
boasvindascomdefault("Andrew")
'''

# Return

def cliente(nome):
    print(f"Olá {nome}")


def cliente1(nome):
    return f"olá {nome}"


nomec = "algum nome"


x = cliente(nomec)
y = cliente1(nomec)

print(x)
print(y)