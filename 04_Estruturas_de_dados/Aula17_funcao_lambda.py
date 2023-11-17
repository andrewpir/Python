

# Lambda function
    # é ma função (pequena) sem nome
    # pode ter varios argumentos mas só uma expressão
    # muito utilizada dentro de outras funções
    # código mais clean


#def somar(x):
#    return x + 10

#print(somar(2))

somar10 = lambda x, y: x + y + 10 # Podemos classificar ela como uma "SUB função"

print(somar10(2, 5))


def multi(x):
    func2 = lambda x: x + 10
    return func2(x) * 4


print(multi(2))