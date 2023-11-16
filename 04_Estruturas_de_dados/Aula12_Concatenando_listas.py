

numeros = [2, 3, 4, 5, 6, 7, 8]
letras = ["a", "b", "c", "d"]

final = numeros * 2
final1 = numeros + letras

numeros.extend(letras)

print(final)
print(final1)
print(numeros)


itens = [["item1", "item2"], ["item3", "item4"]] #Lista dentro de lista [[0,1],[0,1]] e as ids são 0 e 1

print(itens)
print(itens[0][0])
print(itens[0][1])
print(itens[1][0])
print(itens[1][1])

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

#id3 = itens[1][0]
id0, id1, id2, id3, id4, id5, id6, id7 = numbers


print(id0)
print(id1)
print(id2)
print(id3)

id10, id11, *outros = numbers

print(id10)
print(id11)
print(outros)

id10, id11, *outros , id17 = numbers 

print(id10)
print(id11)
print(outros)
print(id17)