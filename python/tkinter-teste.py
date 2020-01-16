#!/usr/bin/env/python
# -*- coding: utf-8 -*-
from Tkinter import *   #importa a bibioteca do TKinter
root = Tk()             #cria a aplicação raiz. 
w = Label(root, text="Teste TKinter!")    #cria um label com o texto especificado
w.pack()                                      #insere na tela
btn = Button(root, text="Olá", cursor="hand2")
btn.pack()
btn2 = Button(root, text="Hello", cursor="umbrella")
btn2.pack()
btn3 = Button(root, text="Hallo", cursor="sailboat")
btn3.pack()
#from Tkinter import ttk
#ttk.Button(root, text="Hello World").grid() #Cria botão
root.mainloop()                               #inicializa o loop