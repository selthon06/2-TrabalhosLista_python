# # aluno = {'nome': 'rogerio', 'nota': 7}
# # print (aluno['nome'])
# # print (aluno['nota'])


# # # adicionando novas chaves e valores
# # aluno['nota2'] = 8
# # aluno['nota3'] = 6
# # print(aluno)



# # aluno = {}  #dicionario em branco
# # aluno['nome'] = 'rogério'   #adicionando a chave para o dicionario
# # aluno['nota'] = 7
# # print(aluno)

# # aluno['nota'] = 9 #adicionando nota
# # print(aluno)


# # del aluno['nota']   #excluir uma chave
# # print(aluno)



# ifms = {'tads': 'python','engenharia_comp': 'c', 'tsi': 'java',}   # exe. chave : tads  , valor : python
# print(ifms)

# # for key, value in ifms.items():   #percorrenco por laço de repeticao,   poderia ser qualquer valor , exe. for chave, valor in ifms.items():
# #     print("\nkey: " + key)
# #     print("Value: " + value)






# for curso, linguagem in ifms.items():          
#     print(curso.title() + " estuda " + linguagem.title())       #title: sempre retorna com a inicial em maiusculo





# for curso in ifms.keys():    #no lucar de items, ele vai retorna as chaves, percorrendo apenas as chaves
#     print(curso.title())

# #é o mesmo que pq é o padrão
# for curso in ifms:      #se nõo colocar nada ele ja retorna por padrao só as chaves
#     print(curso.title())




# # ifms = {'tads': 'python','engenharia_comp': 'c', 'tsi': 'java',}

# # ufms = ['tads', 'tsi', 'informática']
# # for curso in ifms.keys():

# #     #print(curso.title())

# #     if curso in ufms: #poderia ser not in
# #         print(curso.title() + ' existe nas duas instituições')




# for curso in sorted(ifms.keys()):   #so ordenando
#     print(curso.title())



# ifms = {'tads': 'python', 'engenharia2': 'python', 'engenharia_comp': 'c', 'tsi': 'java',}
# print(ifms)
# print()

# for linguagem in ifms.values():   #percorreu retornando apenas o valor, e se colocar 'items' ele retorna chave e valor 
#     print(linguagem.title())

# print()    


# for linguagem in set(ifms.values()):    #ele retorna os elementos uma unica vez, se tiver repetido, ele retorna o primeiro e ignora o segundo.;
#     print(linguagem.title())




# aluno = {'nome': 'rogerio', 'nota': 7}
# aluno1 = {'nome': 'ana', 'nota': 9}
# aluno2 = {'nome': 'josé', 'nota': 9}

# alunos = [aluno, aluno1, aluno2]
# for a in alunos:
#     print(a)


# print()

# alunos= [] 
# for i in range(10):
#     novo_aluno = {'nome': 'teste', 'nota': 6}
#     alunos.append(novo_aluno)

# print("Total de alunos: " + str(len(alunos)))
# print()

# for a in alunos[:3]:
#     print(a)







# ifms = {
#     'curso': 'tads',
#     'disciplinas': ['algoritmos', 'banco de dados', 'empreendedorismo'],
# }

# for disc in ifms['disciplinas']:
#     print(disc)




# ifms = {
#     'tads': ['algoritmos', 'banco de dados', 'empreendedorismo'],
#     'inf': ['português', 'matemática', 'química'],
# }

# for curso, disciplinas in ifms.items():
#     print('\n' + curso.title())
#     for d in disciplinas:
#         print('\t' + d.title())




# Aninhamento: Dicionário dentro de outro dicionário
# local: chave externa ('ifms', 'ufms')
# informacoes: dicionário interno contendo os dados de cada local

# instituicoes = {
#     'ifms': {
#         'nome_curso': 'tads',
#         'tipo_curso': 'superior',
#     },
#     'ufms': {
#         'nome_curso': 'medicina',
#         'tipo_curso': 'superior',
#     }
# }

# for local, informacoes in instituicoes.items():
#     print("\nLocal: " + local)
#     print("Curso: " + informacoes['nome_curso'])
#     print("Tipo do Curso: " + informacoes['tipo_curso'])
    
    
    # Criar um cadastro de alunos utilizando dicionarios o sistema deve ter :
    #   - 1 menu para o usuario escolher as opçoes 
    #   - o usuario deve podwer adicionar um novo aluno;
    #   - pode remover um aluno que ele escolher; 
    #   - pode solicitar a impressao da média de todos os alunps;
    #   - pode solicitar o nome do aluno vcom a maior media
    #   - deve ter uma opção de parada. saida
    
alunos = {}
adicionar = 0
aluno_contador = 0
nota_contador = 0
print("<<<<<<<<<<  MENU  >>>>>>>>>")
def sistema_academico():
    for adicionar in alunos:
        if adicionar == 1:
            adicionar_aluno = input(f"nome do aluno {aluno_contador}: ")
            alunos+=aluno_contador
            adicionar_nota= input(int(f"nota do aluno {nota_contador}: "))
            alunos+=nota_contador
    return sistema_academico

print(sistema_academico)
