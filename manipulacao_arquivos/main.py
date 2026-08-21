import pandas as pd # importa a biblioteca pandas 

dados = pd.read_csv("alunos.csv") # guarda o csv dentro de uma variável

alunos = dados ['nome']
print(alunos)

total_alunos = len(alunos) # pega a quantidade de alunos
print(f"O total de alunos é: {total_alunos}")

# Pega maior nota usando max()
maior_nota = max(dados['nota'])
print(f"A maior nota é de: {maior_nota}")


#Soma das notas usando sum()
soma_notas = sum(dados['nota'])
media_notas = soma_notas / total_alunos

print(f"A média de notas é {media_notas:.2f}")

# Verifica se o aluno está ativo

aluno_ativo = dados[dados['ativo'] == True]['nome']  #Verifica se a coluna "ativo" é True
print(f"Os alunos ativos são: {aluno_ativo}")