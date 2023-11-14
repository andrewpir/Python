

#for com if

# enviar email de compra online
# maximo 3 tentartivas
compra_confirmada = True

dados_compra = "Compra no valor x e entrega confirmada"

for enviar in range(3):
    if compra_confirmada:
        print(dados_compra)
        print("detalhes da compra")
        break
else:
    print("falha na compra")
    
    
#nested loops
#Matrizes
#outerloop
    #inner loop
    
for numero1 in range(5):
    print(f"Produto {numero1}")
    for numero2 in range(5):
        print(numero1 , numero2)
    


#Separando Strings

#Palavra com espaço entre as letras

palavra = "fantastico"

for spaco in palavra:
    print(spaco, end=" ")

print()

for spaco in palavra:
    print(f"{spaco} ", end="")
    
print()

# fazendo um retangulo 6x6

linhas = 6
colunas = 6
simbulos = "#"

for i in range(linhas):
    for j in range(colunas):
        print(simbulos, end=" ")
    print()

print()

#while loop

valor = 100
dia  = 1

while valor > 20:
    print(f"Valor {valor} no dia {dia}")
    valor -= 5
    dia += 1


#operadores Ternários

idade = input("Digite sua idade: ")
idade = int(idade)
'''
if idade >= 16:
    resultado = "Voto permitido"
else
    resultado = "voto não permitido"
'''
resultado = "voto permitido" if idade >= 16 else "voto não permitido"

print(resultado)


