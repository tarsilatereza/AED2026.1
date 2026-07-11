# Criação da lista

class ListaOrdenada():
	def __init__(self):
		self.inicio = None
	myList = ListaOrdenada()

# Definição dos ponteiros atual, previo, parar

def Inserir(self, item):
	atual = self.inicio
	previo = None
	parar = False
	# loop para a inserção - vai percorrer enquanto houver valores para "atual" e "parar" for falso
	while atual != None and not parar:
		if atual.getValor() > item:
			parar = True
		else:
			previo = atual
			atual = atual.getProximo()
			temp = No(item)
		if previo == None:
			temp.setProximo(self.inicio)
			self.inicio = temp
		else:
			temp.setProximo(atual)
			previo.setProximo(temp)



		