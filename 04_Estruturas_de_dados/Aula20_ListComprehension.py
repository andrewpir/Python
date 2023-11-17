

#usado quando vc precisa criar uma lista a partir de uma existente

frutas1 = ["abacate", "banana", "morango", "kiwi", "abacaxi"]
#frutas2 = []

#for iten in frutas1:
#    if "b" in iten:
#        frutas2.append(iten)

frutas2 =[iten for iten in frutas1 if "b" in iten]

print(frutas2)

print(list(iten for iten in frutas1 if "b" in iten))



#valores = []

#for x in range(6):
#    valores.append(x * 10)

valores = [x * 10 for x in range(6)] # nome da lista = [ EXPRESSÂO(o que tem que fazer) for x in range ]

   
print(valores)

print(list(x * 10 for x in range(6)))