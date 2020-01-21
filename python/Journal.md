# Journal
## Introdução
Neste arquivo irei colocar as atividades realizadas durante o desafio dos 100 dias de programação em Python.

## Day 1

* Iniciei criando o repositório no GitHub e testando a biblioteca do TKinter, que é uma biblioteca gráfica. 
* Dei os primeiros passos com um Hello World Apenas. 
* Criei o arquivo tkinter-teste.py

## Day 2

* Tive a ideia de começar um diário para monitorar meu aprendizado. 
* Avancei no estudo da Biblioteca do tkinter. 
* Comecei o código de uma calculadora. 

## Day 3

* Tomei algumas notas do manual do python

'
 O pacote Tkinter ou Interface é uma interface padrão no Python para o Tk GUI. Tanto o Tk quanto tkinter estão dispon[iveis na mairoia   das plataformas Unix e Windows também.

 A interface Tk fica localizada em um módulo binrio chamado de _tkinter. Esse módulo contém a interface de baixo nível do Tk e nunca deve ser usada diretamente pela aplicação do programador. Ela é normalmente compartilhada através da biblioteca (ou DLL), e é normalmente ligada estaticamente com o interpretador do Python.

 Além do módulo de interface Tk, o tkinter inclui diversos módulos Python, como tkinter.constants, umas das mais importantes.  

 tkinter.Tk = A Classe TK é instanciada sem argumentos. Isto cria um widget na camada superior do Tk que normalmente é a janela principal da aplicação. Cada instancia possui seu próprio interpretador TCL associado. 
 tkinter.Tcl = A funçao Tcl() é uma função factory que cria um objeto parecido com o criado pela funçao Tk, exceto por não iniciar um subsitema Tk. Isso é frequentemente útil quando guiamos o interpretador TCL em um ambiente onde não se quer criar janelas superficiais extras, ou onde não pode (Unix sem um X server). Um objeto criado pelo objeto Tcl() pode ter uma janela toplevel criada (e o Tk subsitem inicializado), chamando se o método loadtk().
'
* Posso usar o próprio código do Tkinter para estudar mais: /usr/lib/python3.6/tkinter

## Day 4

* Descobri que colocando o lambda dentro do command e chamando a função ele consegue trocar o valor da entrada, sem precisar mexer em nada na função.
* Sei que o self, quer dizer que estou usando um argumento, ou objeto pertencente aquela classe e se não usá-lo ele procura uma variável global, mas não entendi muito bem pq chamá-lo semrpre no argumento, tenho que pesquisar isso.

## Day 5

* Adicionei a operação de soma e subtração
* Preciso acertar a questão da expressão
* Resolver a questão de operadores em sequencia e também operação com zero que deve dar zero. 

## Day 6

* Resolvido o problema do zero a esquerda.
* Resolvido não colocar dois operadores em sequência.
* Botão de igual resolvendo a equação no display, utilizando função eval.
* Estudar melhor a função eval.

## Day 7

* Inseri as operaçõe de divisão e multiplicação
* Preciso ajustar o layout para ficar com os numeros abaixo do visor. Par isso precisarei criar 2 frames, pois não posso misturar o grid
    e o Pack, eles irão concorrer e não vai funcionar.
* Adicionei a função de ponto para trabalhar com números reais.
* Adcionei um try no eval() para casos em que a expressão esteja mal formatada.
* Finalizar questão de layout que não é tanto o foco do meu aprendizado e inserir parentisis. 

## Day 8

* Adicionado parentesis.
* Adicionado Backspace.
* Reposicionei botões.
* Estudo Tkinter
    '
    Tk/Tcl são partes integrais do Python, possui uma fermanta para criação da layouts de janela robusta e independente, através do pacote tkinter, e suas extensões tkinter.tix e tkinter.ttk
    O tkinter é uma pequena camada  orientada a objetos sobre o Tcl/Tk. Para usar  o Tkinter náo precisa escrever código Tcl, mas precisará consultar a documentação do Tk e ocasionalemnte do Tcl. o Tkinter é uma série de wrappers que implementa os widgets do Tk como classes em Python. E os módulos internos do _tkinter fornecem um mecanismo seguro para o pyhon interagir com o Tcl.

    Além do Tk existem outros pacotes de GUI disponíveis para Python.

    ... (CONTINUAR EM Quick Look Tcl/Tk)

## Day 9

* Quick Look TCL/TK 
> As classes tem o objetivo de organizar certas funções sobre um            namespace. Elas não foram criadas para serem instanciadas de forma          independente.
>    A classe Tk foi pensada para ser instanciada apenas uma vez na aplicação. Os programadores podem não instanciar uma explicita, o sistema cria uma independente de qualquer outra classe ser instanciada. 
>    A classe widget não foi criada para ser instanciada, foi criada apenas para as subclasses criarem widgets reais. No c++ seria uma classe abstrata. 
>    O ideal para trabalhar com esse pacote é conhecer algumas passagens de Tk e como identificar as varias partes do comando TK. (https://docs.python.org/3/library/tkinter.html#tkinter-basic-mapping)
>   Os scripts Tk são programas Tcl, isto é, são apenas listas de tokens separada por espaços. O Tk Widget é apenas uma classe, as opções ajudam a configurá-los e as ações tornam as coisas úteis. 
> Para criar um Widget no Tk, o comando tem a seguinte forma:
>  - classCommand newPathname options
> **classCommand**: Tipo do widget (botão, label, menu, etc..)
> **newPathname**: É o novo nome para o Widget, todos os nomes no Tk devem ser únicos. Funcionam igual a um arquivo em um sistema de arquivos. O widget do nível mais alto é o root, é chamado pelo '.' (periods) e seus filhos são delimitados por mais periods. Por exemplo: .myApp.controlPanel.okButton, pode ser o nome de um Widget.
> **options**: Configura a aparência de um widget e em alguns casos seu comportamento. As opções vem em forma de lista de flgs e valores. Flags são preceddas por '-', como em comandos Unix, e valores são colocados entre aspas duplas se for mais de uma palavra.
> Ex: button.fred -fg red -text "Olá mundo"
> Uma vez criado o pathname para o widget se torna um novo comando. Este novo comando é permitido ter um novo widget para gerar alguma ação. Em C, seria expresso como someAction(fred, someOption), em C++, expressaria algo do tipo fred.someAction(someOption), em Tk seria:
> - .fred someAction someOptions
> Notar que o nome do objeto fred inicia com um ponto. Como experado os valores para someAction dependerá da class do widget: .fre disable funciona se fred for um botão, mas não funciona se fosse um label. Os valores válidos para someOption são dependentes da ação. Algumas ações como disable, não precisam de argumentos, outras como o comando delete em entradas de texto, precisam de argumentos específicos sobre qual parte do texto quer que delete.

## Day 10

* Mapeamento básico Tk no Tkinter 
> O comando de Class no TK corresponde aos construtores de classe no Tkinter.
> button .fred ====> fred = Button()
> A configuração de opções no Tk são dadas em listas de tags refinadas seguidas por seus valores. No Tkinter, opções são especficadas como argumentos chaves no contrutor de instância e os argumntos chaves para configurar chamadas ou os indices de instâncias, no estilo do dicionário, para estabelecer instâncias. 
> No Tk para executar a ação no Widget, use o nome do widget como comando,seguido pelo nome da ação.  In Tinker nós chamados métodos na classe da instancia para invocar ações no widget. As ações (métodos) que um widget pode executar estão listadas em tkinter/__init__.py
> Para dar um widget ao packer(gerenciador de geometria), é preciso chamar o pack com argumentos opcionais. In Tkinter, a classe pack possui todas as funcionalidade e as várias formas do comando pack são implementadas como métodos. Todo os widgets in tkinter são subclasses do Packer e implementa todos os métodos. Ver o tkinter.tix(https://docs.python.org/3/library/tkinter.tix.html#module-tkinter.tix) para documentação adicional do Form Geometry manager. 

* Como Tk e Tkinter se relacionam
> Seguindo uma avaliação top down.
> App(Python): uma aplicação python faz uma chamado ao tkinter.

> tkinter (Python Package): chama um botão por exemplo, implementado no tkinter package, que é escrito em python. Essa função de Python irá analisar os comandos e argumentos e convertê-los em uma forma que faça parece que eles vieram de um Tk script ao invé de um script Python.

> _tkinter(C): esse comando e seus argumetnos serão passados para uma função C no _tkinter . O "_" indica um módulo de extensão.

> Wk Widgets (C e TCL): Essa função C é capaz de fazer camadas em outros módulos C, incluindo as funções C que fazem parte da biblioteca Tk. Tk é implementado em C e algo em Tcl. A parte do Tcl dos Tk widgets sáo usadas para vincular alguns comportamentos padrões aos widgets, e é executado uma vez que o pacote Tkinter do python é importado.

> Tk (C):  parte Tk dos Tk Widgets implementa o mapeamnto final para ..

> Xlib(C): A biblioteca xLib desenha os gráficos na tela. 

## Day 11

* Referencias úteis
> O controle de opçẽs como cor e larguda da borda, pode ser feito de três formas:
> * no momento de criação do objeto
> fred = Button(self, fg="red", bg = "blue")
> * Após a criaçào do objeto:
> fred["fg"] = "red"
> fred["bg"] = "blue"
> * Utilizando o método config(), para atualizar múltiplos atributos, depois da criação do objeto.
> fred.config(fg="red", bg = "blue")

> Para uma explicação maior sobre as opções o ideal é ver o manual do Tk para cada Widget. 
> As páginas man listam os "STANDARD OPTIONS" e "WIDGET SPECIFIC OPTIONS" para cada widget. O primeiro é uma lista de opções que sáo comuns em vários widgets, o segundo são opções únicas referentes de cada widget.As opções padrão dos widgets estao: https://manpages.debian.org/options(3)
> Não há distinção entre as  opções padrões e específicas de um widget, feita neste documento. Algumas opções não se aplicam a alguns tipos de widgets. Se um widget responde a uma opção particular, ela depende da classe do widget. Botões tem a opção comando, labels não. 
> A opção suportada por um dado widget são listadas na man page do widget, ou podem ser perguntadas utilizando a chamada config() utilizado sem argumentos, ou chamando keys() no widget. O valor de retorno dessa chamada será um dicionário nos quais as chaves são os nomes das opções como uma string e esses valores são 5-tuplas.
> Algumas opções, como bg são sinônimos para opções comuns para nomes grandes. Passando o nome do método config() de uma opção curta retornará uma 2-nupla, não 5-tupla. A 2-tupla passada de volta contém o ome do sin^nimo e da opção real.
* Exemplo:
> print(fred.config())

## Day 12  

* O Packer
> É um dos mecanimos de gerenciamento de geometria (Design) do Tk. Os gerenciadores de geometria são usados para especificar o posicionamento relativo das posições dos widgets dentro dos containers - E seus respectivos masters. Em contraste com gerenciadors mais pesados, o packer possui uma especificação mais amigável (above, to the left, filling, etc) e faz tudo funcionar e determina o lugar exeato as coordenadas.
> O tamanho de qualquer widget é determinado pelo tamanho do "slave widget" interno. O Packer é usado para controlar onde os slaves apereceram dentro do master nos quais eles fazem parte. Você pode empacotar widgets em frames, e frames em outros frames, conseguindo obter o layout que quiser. Além disso, o layout é dinamicamente ajustado para acomodar mudanças incrementais a configuração, uma vez empacotado. 
> Note que os widgets não aparecerão até eles terem sua geometria especificada com um gerenciador. É comum um erro iniciante, de esquecer a especificação da geometrua e se surpreender quando nada acontecer mesmo criando o widget. 
> O pack() pode ser chamado utilizando algumas palavras chaves que o ocntrolam, onde o widget que aparece dentro do contauner, e qual o comportamento quando a janela da aplicação é redimensionada. 

* Exemplos:
> fred.pack()
> fred.pack(side="left")
> fred.pack(expand=1)

## Day 13
* Opções do Packer
> + infos packer: MAN pages e pag 183 do livro do Ousterhout.
> * anchor: Denota onde o packer será colocado e seus slave.
> * expand: Boleano 0 ou 1
> * fill: valores utilizados: x,y,both,none
> * ipdax e ipday: distancia do espaçamento interno em cada lado do slave widget. 
> * padx e pady: distância de espaçamento externa em cada lado do slave widget.
> * side: valores utilizados: left,right, top, bottom.

## Day 14

* Variáveis de ligação dos widgets
> O valor configurado de alguns widgets (como entrada de texto), podem ser conectados diretamente a variáveis usando opções especiais. Essas opções são:  **variable, textvariable, onvalue, offvalue e value**. Essa conexão funciona em ambos os sentidos. Se a variável mudar o widget ligado a ela será atualizado, refletindo o novo valor. 
>Infelizmente, na implementação atual do tkinter não é possível atuar sobre uma variável do python com um um widget através das opções **variable ou textvariable**. A única forma que funciona são variáveis como subclasses de uma classe chamada **Variable** do tkinter.
> Existem muitas subclasses da classe Variable já definidas: StringVar, IntVar, DoubleVar e BooleanVar. Para ler valor atual de alguma variável, chame o método get() e mude seu valor utilizando o método set(). Seguindo esse protocolo, o widget sempre irá seguir o valor da variável, sem necessidade de mais intervenções.
* Ex:
> class App(Frame):
>  def __init__(self, master=None):
>   super().__init__(master)
>   self.pack()
>   self.entrythingy = Entry()
>   self.entrythingy.pack()
>   #Variável da aplicação
>   self.contents = StringVar()
>   #Adicionando valor a variavel
>   self.contents.set("Valor variável")
>   #Associando a entrada do widget a variável.
>   self.entrythingy["textvariable"] = self.contents
>   #Pega um callback quando o usuário clica. 
>   #O programa imprime o valor da variável da aplicação quando o usuário clica.
>   self.entrythingy.bind(' <Key-Return>', self,print_contents)
>  def print_contents(self, event):
>   print(" O conteúdo da entrada agora é -->", self.content.get())
 
* Gerenciador de janelas
> No Tk o **wm** é um comando útil para interagir com o gerenciado de janelas. AS opções do wm permitem controlar coisas como titles, placement, icon, bitmaps e etc. No tkinter, esses comandos são implementados como métodos da classe Wm. 
> Para obter uma janela na camada superior com um dado widget, é preciso apenas referenciar o widget ao mater Claro se o widget estiver empacotado dentro de um grame, o master não será representado como a janela superior. Para isso é necessário chamar o método _root(). Este méotodo começa com o underline para denotar o fato que essa função faz parte da implementação, e não ná funcionadlidade da interface Tk.

* Ex
> import tkinter as tk
>
>class App(tk.Frame):
>    def __init__(self, master=None):
>        super().__init__(master)
>        self.pack()
>
>#create the application
>myapp = App()
>
>#here are method calls to the window manager class
>
>myapp.master.title("My Do-Nothing Application")
>myapp.master.maxsize(1000, 400)
>
>#start the program
>myapp.mainloop()
 
## Day 15

* Tk tipos de opções
> * anchor: valores válidos são pontos da bússula: "n", "ne", "e", "se", "s", "sw", "w" e "nw" e também o "center".
> * bitmap: Existem 8 tipos de bitmpas internos: "error", "gray25", "gray50", "hourglass", "info", "questhead", "question", "warning". Para especificar o nome do arquivo do bitmap, deve-se colocar o nome completo do arquivo precidido por @:
> * boolean: passa inteiros 1 ou 0, ou então strings "yes"ou "no".
> * callback: É qualquer funçao em Python que não possui argumentos.
Ex:
> def print_it():
>   print("Olá mundo")
> fred["command"] = print_it
> * color: As cores podem ser escolhidas com os nomes no arquivo rgb.txt, ou com strings representando os calores em 4 bits: "#RGB", 8 bits: "#RRGGBB", 12 bits: "#RRRGGGBBB" ou 16 bit: "#RRRRGGGGBBBB", onde cada letra R,G,B representa qualquer valor heaxdecimal. 
> * cursor: O nome padrão do cursor X, cursorfont.h, pode ser usado, sem o prefixo XC_. Por exemplo para ter um cursos de mão (XC_hand2), usa a string "hand2". Pode especifica também, um bitmap e um arquivo de máscara próprio. 
> * distance: As distâncias na tela, podem ser especificadas em pixels ou distâncias absolutas. Pixels são dados como números e distâncias absolutas como strings, com o caracter denotando a unidade, 'c' para centimetros, 'i' para polegadas, 'm' para milimetros e 'p' para pontos de impressão.
> * font: Tk usa o formato de lista de fonte como {courier 10 bold}. Tamanhos de fontes com números positivos sáo medidos em pontos, tamanhos com números negativos em pixel. 
> * geometry: É uma string da forma 'widthxheight', onde a largura e altura sáo medidas em pixel na maioria dos widgets. Ex: fred["geometry"]="200x100"
> * justify: Pode utilizar os seguintes valores: "left", "center", "right" e "fill".
> * region: Esta é uma string com elementos delimitados por espaço, cada um é uma distância válida. 
> * relief: determina o estilo da borda do widget. Valores válidos: "raised", "sunken", "flat", "groove" e "ridge"
> * scrollcommand: quase sempre o set() de algum widget com scrollbar, mas pode ser qualquer método de widget que tenha um único argumento. 
> * wrap: Deve ser um dos: "none", "char" ou "word"

* Fiz alguns testes com as opções acima, utilizando cursores.

## Day 16

* Bindings e eventos

> O método biding do comando do Widget permite ver certos eventos e ter um trigger para função de callback , quando aquele evento ocorrer. A forma do método é:
> def bind(self, sequence, func, add = ''):

> * sequence: é uma string que denota o alvo de cada evento. 
> * func: é uma função python com um argumento, que é chamada quando o evento ocorre. Uma instância do evento é passada como argumento. (Funções deste tipo normalmente são chamadas de callback.)
> * add: é opcional, '' ou '+'. Passando uma string vazia denota que esse binding é para subtituir qualquer outro binding ao qual o evento esteja associado. 
Ex:
> def turn_red(self,event):
>    event.widget["activeforeground"] = "red"
> self.button.bind("<Enter>", elf.turn_red)

* O paâmetro index

> Varios widgets precisam que passe um parâmetro de "index". Eles sáo usados para apontar um lugar espec[ifico no widget de teste, ou um caracter em particular em um widget de enrada, ou um item do menu em um widget menu. 

> * index em widgets de entrada (index,view index, etc): tem a opção de referenciar a posição do caracter no texto exibido. Você pode usar as funções para acessar esses pontos especiais nos widget de textos.
> * index em widgets de texto: é bem descrito no Tk man pages.
> * index menus (menu.invoke(), menu.entryconfig(), etc): Algumas opções e métodos de menus manipual entras especificas doles. De qualquer jeito o index do menu é necessário para uma opção ou parâmetro, que deve passar em:
> - Um inteiro que referencia numericamente a posiçõa da entrar n widget, contado do topo, iniciando em 0.
> - a string "active", que que referencia que a posição atual abaixo do cursor. 
> - a strig "last", se refere a o último item do menu. 
> - Um inteiro precedido por '@', como @6, o inteiro é interpretado omo a coordenada y no sistema de coordenadas do menu. 
> - a string "none" indica que não há entrada no menu, frequentemente usado com menu.active() para desativar todas as entradas.
> - uma string de texto, que é um padráo comparado ao label de entrada do menu, é como se fosse varrer do topo a pate debaixo do mneu. Esse tipo de index é considerad depois de todos os outros, o que significa que encontra items etiquetados com "last","active" ou "none", serão interpretados como os items acima. 

## Day 17

* Images
> Imagens de diferentes formatos podem ser criadas a patir da subclasse tkinter.Image
> * BitmapImage para imagens com formato XBM.
> * PhotoImage para imagens em formato PGM, PPM, GIF e PNG. 
> O tipo da imagem é criado tanto pelo "file" quanto pela opção "data".
> O objeto da imagem pode ser usado para qualquer widget que suporte a opção de imagem (labels, buttons, menus). Nesses casos, o Tk náo manterá a referência da imagem. QUando a última referência no Python do objeto da imagem [e deletado, os dados da imagem são deletados também, e o Tk exibirá uma caixa vazia, onde a imagem aparecia.
> O pacote "Pillow" adiciona o suporte a outros tipos de imagem como BMP, JPEG, TIFF e Webp, entre otras.

* File Handlers (Manioulador de arquivos)
A temporary reference (typically a number) assigned by the operating system to a file that an application has asked it to open. The handle is used throughout the session to access the file.
> O File Handler é uma referencia (normalmente um número), atribuído pelo sistema operacional a um arquivo que uma aplicação pediu para abrir.
> O Tk te permite registrar e desregistrar uma função de callback, que pode ser chamdado do loop principal do Tk, quando é possível realizar um I/O no arquivo. Apenas um handler pode ser registrado em cada descritor de arquivo.
Ex:
> import tkinter
> widget = tkinter.Tk()
> mask = tki\nter.READABLE | tkinter.WRITABLE
> widget.tk.createfilehandler(file,mask,callbak)
> wdget.tk.deletefilehandler(fil

> Essa função não está disponível para Windows.

> Como você não sabe quantos bytes estão disponíveis para leitura, não vai querer usar os métodos BufferedIOBase ou TextIOBase read() ou o readline(), já que precisam ler um número pré definido de bytes. Para sockets, o recv() ou o recvform() funcionarão corretamente, para outros arquivo usar o leitor base ou os.read(file.fileno(), maxbytecount).

> * Widget.tk.createfilehandler(file, mask, func): Registra a função callback "func" do file handler. O argumento "file" pode ser um objeto com o método fileno()(file ou socket), ou um descritor de arquivo inteiro. O argumento mask é uma combinação ORed, de qualquer das três constantes abaixo. O callback é chamado na forma:
> callback(file,mask)

* Widget.tk.deletefilehandler(file): desregistrar um file handler.
> * tkinter.READABE
> * tkinter.WRITABLE
> * tkinter.EXCEPTION

## Day 18

* Testei o uso de fram do Tkinter
* Alinhei os frames do tkinter-teste.py com grid e com pack.
* Comecei a implementar no calculadora, mas sem sucesso.
* Estava dando o erro, pois como lá estou colocando uma classe, não sei quem seria o root.
* Criei o calculadora 2 para testar usando 2 frames.

## Day 19

* Inseri menu na Calculadora
* Criei os frames para alinhar bem os botões.
* Finalizei a calculadora, como Calculadora2.py

## Day 20

* Hoje começarei a documentar o estudo de BI.
* Fazer alguns dos exercícios do Kaggle e dar continuidade ao curso da Data Science Academy
* Finalizei a criação de um modelo de predição de preços de casa. 
* Todas as informações coloquei no jupyter_notebook, BI.ipynb
