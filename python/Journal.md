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

* Add Day 9
* 


