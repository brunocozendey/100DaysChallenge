#!/usr/bin/env/python
# -*- coding: utf-8 -*-
from Tkinter import *   #importa a bibioteca do TKinter
root = Tk()             #cria a aplicação raiz. 
w = Label(root, text="Teste TKinter!")    #cria um label com o texto especificado
w.pack()                                      #insere na tela
#from Tkinter import ttk
#ttk.Button(root, text="Hello World").grid() #Cria botão
root.mainloop()                               #inicializa o loop
