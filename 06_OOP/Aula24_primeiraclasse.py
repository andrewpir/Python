from datetime import datetime


'''
class Funcionarios:
    nome = "Elena"
    sobrenome = "Cabral"

usuario1 = Funcionarios()

print(usuario1.nome)
print(usuario1.sobrenome)
'''

'''#criar classe
class Funcionarios:
    pass
    
#criar o Objeto
usuario1 = Funcionarios()
usuario2 = Funcionarios()

#criar os parametros do usuario 1
usuario1.nome = "Elena"
usuario1.sobrenome = "Cabral"

#criar os parametros do usuario 2
usuario2.nome = "Durex"
usuario2.sobrenome = "Pirox"

#Print
print(usuario1.nome)
print(usuario1.sobrenome)

print(usuario2.nome)
print(usuario2.sobrenome)
'''
# CRIANDO CONSTRUCTORS
#criar classe
class Funcionarios:
                #Objeto, argumentos
    def __init__(self, nome, sobrenome, ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento

    def nome_completo(self):
        return self.nome + " " + self.sobrenome

    def idade_funcionario(self):
        ano_atual = datetime.now().year
        self.idade = int(ano_atual - self.ano_nascimento)
        return self.idade
        
        
#criar o Objeto
usuario1 = Funcionarios("Elena", "Cabral", 2009)
usuario2 = Funcionarios("Carol", "Silva", 2005)
usuario3 = Funcionarios("Andrew", "Pires", 1989)

#Print
print(usuario1.nome)
print(usuario1.sobrenome)
print(usuario1.ano_nascimento)

print(usuario2.nome)
print(usuario2.sobrenome)
print(usuario2.ano_nascimento)

print(usuario3.nome)
print(usuario3.sobrenome)
print(usuario3.ano_nascimento)

print(usuario1.nome_completo())

print(Funcionarios.nome_completo(usuario1)) #classe.função(objeto)
print(Funcionarios.idade_funcionario(usuario1))