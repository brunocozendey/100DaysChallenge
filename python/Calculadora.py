#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter
class App(Tkinter.Tk): # Tkinter.tk é a classe base para a janela padrão. A App herda todas as funcionalidades da classe padrão.
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent) # Chamando o construtor da classe pai, Tkinter.Tk.__init__())
        self.parent = parent # Para acessar o pai de um objeto, é uma boa técnica salvar uma referencia ao pai.
        self.initialize()  #no método initialize são criados os demais objetos que serão apresentados na tela, inciailiza as variáveis 
                            #globais (irc..), o hardware caso necessário, etc..
         
    
    def initialize(self): #widgets que serão apresentados na tela
        self.grid()
        self.titulo = Tkinter.Label(self, text="Resultado:")
        self.titulo.grid(column=0,row=0)          
        self.entrada = Tkinter.Entry(self)           
        self.entrada.grid(column=0,row=1,sticky='EW')
        self.btnUm = Tkinter.Button(self,text="1",command=self.OnButtonNumClick(1))
        self.btnUm.grid(column=1,row=2)
        self.btnDois = Tkinter.Button(self,text="2",command=self.OnButtonNumClick(2))
        self.btnDois.grid(column=2,row=2) 
        self.btnTres = Tkinter.Button(self,text="3",command=self.OnButtonNumClick(3))
        self.btnTres.grid(column=3,row=2) 
        self.btnQuatro = Tkinter.Button(self,text="4",command=self.OnButtonNumClick(4))
        self.btnQuatro.grid(column=4,row=2)

        self.btnIgual = Tkinter.Button(self, text="=", command=self.OnButtonIgualClick())
        self.btnIgual.grid(column=1, row=3)

    def OnButtonNumClick(self,n):    
        #fCent= float(self.entryC.get())
        #fFar= (9.0 * fCent )/5 + 32.0 
        self.entrada.delete(0,Tkinter.END)
        self.entrada.insert(0,str(n))
    def OnButtonIgualClick(self):
        a = self.entrada.get()
        self.entrada.delete(0,Tkinter.END)
        self.entrada.insert(0,str(a*2))

if __name__ == "__main__":
    app = App(None)
    app.title("..:: Calculadora ::..")
    app.mainloop()