import os
import ast

PECAS = "data/pecas.dat"
MAX_TOTAL_REGISTROS = 50

#limpar tela
def limpar_tela():
	try:
		os.system('clear')
	except:
		os.system('cls')

#iniciar arquivo
def init():
	try:
		arquivo = open(PECAS, 'a')
	except:
		arquivo = open(PECAS, 'w')

	arquivo.close()
	menu()

#menu principal
def menu():
	opcoes = ["Incluir", "Listar", "Sair"]
	acao = 0

	while True:
		limpar_tela()
		print "MENU PRINCIPAL"
		print "----------------------------------"
		
		for index, value in enumerate(opcoes):
			print "{0}) {1}".format((index + 1), value)

		acao = int(raw_input("\nEscolha uma das opcoes: "))

		if acao == 1:
			incluir()
		elif acao == 2:
			listar()
		elif acao == 3:
			exit()

#incluir um novo registo
def incluir():
	limpar_tela()

	arquivo = open(PECAS, 'r')
	pecas = arquivo.readlines()
	pecas_cadastradas = len(pecas)


	print "INCLUIR PECA {0}/{1}".format(pecas_cadastradas, MAX_TOTAL_REGISTROS)
	print "----------------------------------"

	if pecas_cadastradas < MAX_TOTAL_REGISTROS:
		codigo = int(raw_input("Codigo: "))
		peca = raw_input("Peca: ")
		descricao = raw_input("Descricao: ")
		quantidade = int(raw_input("Quantidade: "))
		preco = float(raw_input("Preco: "))

		peca_lista = {'codigo': codigo, 'peca': peca, 'descricao': descricao, 'quantidade': quantidade, 'preco': preco}
	
		arquivo = open(PECAS, 'a')
		arquivo.write(str(peca_lista) + '\n')
		arquivo.close()
	else:
		print "Numero maximo de {0} registros foi atingido".format(MAX_TOTAL_REGISTROS)
		raw_input()


#listar registos
def listar():
	limpar_tela()
	
	pecas = open(PECAS, 'r').readlines()
	total_pecas_unicas = 0
	pecas_cadastradas = len(pecas)

	print "LISTAR PECA {0}/{1}".format(pecas_cadastradas, MAX_TOTAL_REGISTROS)
	print "----------------------------------"

	if pecas_cadastradas > 0:
		for index, peca in enumerate(pecas):
			p = ast.literal_eval(peca)
			print "{0}) {1} | {2} | {3} | {4} | {5}".format(index + 1, p["codigo"], p["peca"], p["descricao"], p["quantidade"], p["preco"])
			total_pecas_unicas += int(p["quantidade"])

		print "----------------------------------"
		print "TOTAL Pecas unicas: {0}".format(total_pecas_unicas)

		try:
			acao = int(raw_input("\n1) Excluir. 2) Voltar: "))

			if acao == 1:
				excluir()
			elif acao == 2:
				menu()
		except ValueError:
			menu()
	
	else:
		print "Nenhuma peca cadastrada"
		raw_input()

#editar registo
def editar():
	print "EDITAR PECA"
	print "----------------------------------"
	#TODO Editar
	raw_input()

#ecluir registo
def excluir():
	try:
		codigo = int(raw_input("\nCodigo do Produto: "))

		pecas = open(PECAS, 'r').readlines()
		pecas_salvar = []

		for peca in pecas:
			p = ast.literal_eval(peca)
			if int(p['codigo']) != codigo:
				pecas_salvar.append(peca)

		
		arquivo = open(PECAS, 'w')
		arquivo.writelines(pecas_salvar)
		arquivo.close()

	except ValueError:
		print "Codigo invalido"
		excluir()

#inicializar o app
init()
