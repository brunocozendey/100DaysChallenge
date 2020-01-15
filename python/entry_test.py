class App(Frame):
	def __init__(self, master=None):
   		super().__init__(master)
   		self.pack()
  		self.entrythingy = Entry()
   		self.entrythingy.pack()
   		#Variável da aplicação
   		self.contents = StringVar()
   		#Adicionando valor a variavel
  		self.contents.set("Valor variável")
   		#Associando a entrada do widget a variável.
   		self.entrythingy["textvariable"] = self.contents
   		#Pega um callback quando o usuário clica. 
   		#O programa imprime o valor da variável da aplicação quando o usuário clica.
   		self.entrythingy.bind(' <Key-Return>', self,print_contents)
	def print_contents(self, event):
   		print(" O conteúdo da entrada agora é -->", self.content.get())
