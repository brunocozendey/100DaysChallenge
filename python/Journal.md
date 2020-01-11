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
> tkinter (Python Package): chama um botão por exemplo, implementado no tkinter package, que é escrito em python. Essa função de Python irá  


