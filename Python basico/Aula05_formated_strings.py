

nome = "Andrew"
sobrenome = "Pires"
profissao = "Programador"

texto = "O " + nome + " " + sobrenome + " é um exelente" + " [" + profissao + "] "


texto2 = f"O {nome} {sobrenome} é um exelente [{profissao}]" 


print(texto)

print(texto2)


#metodos para strings

texto3 = "    Eu adoro comida caseira"

print(texto3.upper())
print(texto3.lower())
print(texto3.find("c"))
print(texto3.find("adoro")) #-1 quer diser que não encontrou
print(texto3.replace("a", "e"))
print(texto3.replace("caseira", "feita em casa"))
print(texto3.strip()) # sem os espaços no inicio da string
