#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter as tk

class App(tk.Tk): # Tkinter.tk é a classe base para a janela padrão. A App herda todas as funcionalidades da classe padrão.
    def __init__(self,parent):
        tk.Tk.__init__(self,parent) # Chamando o construtor da classe pai, Tkinter.Tk.__init__())
        self.parent = parent # Para acessar o pai de um objeto, é uma boa técnica salvar uma referencia ao pai.
        self.initialize()  #no método initialize são criados os demais objetos que serão apresentados na tela, inciailiza as variáveis 
                            #globais (irc..), o hardware caso necessário, etc..
        
    
    def initialize(self): #widgets que serão apresentados na tela
        self.grid()
        self.titulo = tk.Label(self, text="Resultado:")
        self.titulo.grid(column=0,row=0)          
        self.entrada = tk.Entry(self) 
        self.entrada.insert(0,str(0))          
        self.entrada.grid(column=0,row=1,sticky='EW')

        self.btnUm = tk.Button(self,text="1",command=lambda: self.OnButtonNumClick(1))
        self.btnUm.grid(column=3,row=4)
        self.btnDois = tk.Button(self,text="2",command=lambda: self.OnButtonNumClick(2))
        self.btnDois.grid(column=2,row=4) 
        self.btnTres = tk.Button(self,text="3",command=lambda: self.OnButtonNumClick(3))
        self.btnTres.grid(column=1,row=4) 
        self.btnQuatro = tk.Button(self,text="4",command=lambda: self.OnButtonNumClick(4))
        self.btnQuatro.grid(column=3,row=3)
        self.btnCinco = tk.Button(self,text="5",command=lambda: self.OnButtonNumClick(5))
        self.btnCinco.grid(column=2,row=3)
        self.btnSeis = tk.Button(self,text="6",command=lambda: self.OnButtonNumClick(6))
        self.btnSeis.grid(column=1,row=3)
        self.btnSete = tk.Button(self,text="7",command=lambda: self.OnButtonNumClick(7))
        self.btnSete.grid(column=3,row=2)
        self.btnOito = tk.Button(self,text="8",command=lambda: self.OnButtonNumClick(8))
        self.btnOito.grid(column=2,row=2)
        self.btnNove = tk.Button(self,text="9",command=lambda: self.OnButtonNumClick(9))
        self.btnNove.grid(column=1,row=2)
        self.btnZero = tk.Button(self,text="0",command=lambda: self.OnButtonNumClick(0))
        self.btnZero.grid(column=2,row=5)

        self.btnSoma = tk.Button(self, text=" . ", command=lambda: self.OnButtonOperClick("."))
        self.btnSoma.grid(column=1, row=5)

        self.btnSoma = tk.Button(self, text="+", command=lambda: self.OnButtonOperClick("+"))
        self.btnSoma.grid(column=2, row=6)
        self.btnSubtracao = tk.Button(self, text="-", command=lambda: self.OnButtonOperClick("-"))
        self.btnSubtracao.grid(column=3, row=6)

        self.btnSubtracao = tk.Button(self, text="*", command=lambda: self.OnButtonOperClick("*"))
        self.btnSubtracao.grid(column=2, row=7)

        self.btnSubtracao = tk.Button(self, text="/", command=lambda: self.OnButtonOperClick("/"))
        self.btnSubtracao.grid(column=3, row=7)

        self.btnIgual = tk.Button(self, text=")", command=lambda: self.OnButtonNumClick(")"))
        self.btnIgual.grid(column=1, row=7)

        self.btnIgual = tk.Button(self, text="(", command=lambda: self.OnButtonNumClick("("))
        self.btnIgual.grid(column=1, row=6)

        self.btnIgual = tk.Button(self, text="=", command=lambda: self.OnButtonIgualClick())
        self.btnIgual.grid(column=3, row=5)

        self.btnClr = tk.Button(self, text="CLR", command=lambda:self.OnButtonClrClick())
        self.btnClr.grid(column=1, row=1)

        self.btnBksp = tk.Button(self, text="<-", command=lambda:self.OnButtonBkspClick())
        self.btnBksp.grid(column=2, row=1)

        self.btnSair = tk.Button(self, text="Sair", fg ="gray", bg="red", command=self.destroy)
        self.btnSair.grid(column=0, row=8)
        
    def OnButtonNumClick(self,n):    
        value = self.entrada.get()
        if value.isdigit():
            if n == 0:
                if (value[-1] in ["+","-","/","*","."]): # para remover o zero a esquerda
                    self.entrada.delete(0,tk.END)
                    self.entrada.insert(tk.END,str(value))
                else:
                    self.entrada.insert(tk.END,str(n))
                
            else:    
                if int(value) == 0:
                    self.entrada.delete(0,tk.END)
                    self.entrada.insert(tk.END,str(n))
                else:
                    self.entrada.insert(tk.END,str(n))
        else:
            self.entrada.insert(tk.END,str(n))

        
    def OnButtonIgualClick(self):
        a = self.entrada.get()
        self.entrada.delete(0,tk.END)
        try:
            self.entrada.insert(0,eval(a)) #eval() resolve qualquer tipo de equação.
        except:
            self.entrada.insert(0,"Err")
        #Implementar o claculo de expressão, terá que ser feito por partes, pensei em fazer como vetor.
        

    def OnButtonBkspClick(self):
        value = self.entrada.get()
        if len(value) == 1:
            self.entrada.delete(0,tk.END)
            self.entrada.insert(0,str(0))
        else:
            self.entrada.delete(0,tk.END)
            self.entrada.insert(0,value[:-1])
    
    def OnButtonClrClick(self):
        self.entrada.delete(0,tk.END)
        self.entrada.insert(0,str(0))

    def OnButtonOperClick(self,operador):
        value = self.entrada.get()
        if (value[-1] in ["+","-","/","*","."]):
            self.entrada.delete(0,tk.END)
            self.entrada.insert(0,value)
        else:
            self.entrada.insert(tk.END,operador)


if __name__ == "__main__":
    app = App(None)
    app.title("..:: Calculadora ::..")
    app.mainloop()