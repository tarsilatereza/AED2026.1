import time

alunos = []
with open('alunos-ativos.txt', 'r', encoding='utf=8') as arquivo:
 	for linha in arquivo:
 		matricula, nome = linha.split('\t')
		# split joga para duas variáveis
 		alunos.append([matricula, nome.replace('\n', '')])

ano_ingresso = input('Informe o ano que você quer pesquisar:')
nome_aluno = input("Informe o nome do aluno: ")
for aluno in alunos:
	matricula, nome = aluno
	ano - matricula[0:4]
	if ano == ano_ingresso:
		nomes = nome.split(' ')
		if nome_aluno in nomes:
			print(nome)

# alunos = []
# with open('alunos-ativos.txt', 'r', encoding='utf=8') as arquivo:
# 	for linha in arquivo:
# 		matricula, nome = linha.split('\t')
# 		# split joga para duas variáveis
# 		alunos.append(matricula, nome.replace('\n', ''))
# 		print(aluno)
# 		time.sleep(1)