
#imprimindo listas
'''
valores = [50, 80, 110, 150, 170, 200]

for i in valores:
    print(f"o valor final do Produto é de {i}")
'''

#if em listas
'''
cor_cliente = input("digite a cor desejada: ")
cores = ["amarelo","verde", "azul", "vermelho"]

if cor_cliente.lower() in cores:
    print("Em estoque")
else:
    print("Não temos essa cor na lista")
    
'''

#palavras virando lista
'''
var = list("comprar")
print(var)
'''

#juntar listas com zip

'''
cores = ["amarelo","verde", "azul", "vermelho"]
valores = [10, 20, 30, 40]

duas_listas = zip(cores, valores) #junta as listas referenciando a ID

print(duas_listas) #imprime algo q n intendi
print(list(duas_listas)) #"descompacta" a lista
'''

#criar uma lista a partir de um imput do usuario
'''
lista_usuario = input("Digite os itens da lista separado por virgula: ")

lista_lista = lista_usuario.split(","or", ")

print(lista_lista)
'''

# TUPLES, são listas que não mudam, elas n aceitam alteração de itens

cores_list = [10, 20, 30, 40]  #lista se define com []
cores_tuple = (10, 20, 30, 40)  #Tuple se define com ()

print(type(cores_list))
print(type(cores_tuple))