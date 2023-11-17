

#dicionarios

vasio = {}
#nome    chave   valor
aluno = {
    "nome": "Ana", 
    "idade": 18, 
    "Nota Final": 7.5, 
    "Aprovação": True, 
    "materias": ["fisica", "matematica", "ingles"]
}
'''
print(aluno)
print(aluno["nome"])


aluno["nome"] = "jorjão"

print(aluno)

aluno.update({"nome": "josé", "Nota Final": 8}) #vantagem de atualizar mais de um campo ao mesmo tempo

print(aluno)

aluno.update({"endereço": "Rua A"}) #Pode se adicionar valores tbm

print(aluno)

print(aluno.get("cidade", "Não Existe")) #retorna none pois não tem, se não encontrar ele emite a mensagem "Não Existe"

#del aluno["nome"] deleta o campo selecionado
'''

#usando Loops

#for i in aluno: #aluno.keys() imprime as chaves / aluno.values() imprime os valores das chaves / aluno.items imprime todas as informações em formato de tuple 
#    print(i)
'''
for keys, values in aluno.items(): # retira os valores e as chaves usando duas variaveis
    print(keys, values)
'''

print(aluno)
print(aluno.get("materias"))
print(len(aluno))
print(aluno.items())
print(aluno.keys())
print(aluno.values())
