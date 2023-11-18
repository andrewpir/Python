

#muito usados em testes
#não para o programa
#mensagens customisadas
'''
try:
    letras = ["a", "b", "c"]
    print(letras[3])
except IndexError:
    print("index não existente")
'''

#try com Input

'''
try:
    valor = int(input("Digite o valor do seu produto: "))
    print(valor)
except ValueError:
    print("Valor Inválido")
    
print("um monte de código")
'''

#try com else e finaly

try:
    valor = int(input("Digite o valor do seu produto: "))
    print(valor)
except ValueError:              #vem quando tem erro
    print("Valor Inválido")
else:                           # vem quando não tem erro
    print("Valor Aceito")
    resultado = valor * 2
    print(resultado)
finally:
    print("um monte de código") #acontece tendo ou não erros


    
print("um monte de código")