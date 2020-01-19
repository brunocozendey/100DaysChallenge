#!/usr/bin/env/python
# -*- coding: utf-8 -*-

from Tkinter import *   #importa a bibioteca do TKinter

def donothing():
    print ('IT WORKED')

root = Tk()             #cria a aplicação raiz. 
root.title(string="..:: CALCULADORA ::..")

frame1 = Frame(root)
#frame1.pack(side=TOP, fill=X)
frame1.grid()

frame2 = Frame(root)
#frame2.pack(side=RIGHT, fill=X)
frame2.grid()
mainmenu = Menu(frame1)
root.config(menu=mainmenu)

submenu=Menu(mainmenu)
mainmenu.add_cascade(label='File',menu=submenu)
submenu.add_command(label='Open', command=donothing)
submenu.add_separator()
submenu.add_command(label='Exit', command=frame1.quit)


w = Label(frame1, text="Teste TKinter!")    #cria um label com o texto especificado
#w.pack()
w.grid(column=0,row=0)                                     #insere na tela
btn = Button(frame1, text="Olá", cursor="hand2")
#btn.pack()
btn.grid(column=0,row=1)
btn2 = Button(frame2, text="Hello", cursor="umbrella")
#btn2.pack()
btn2.grid(column=0,row=0)
btn3 = Button(frame2, text="Hallo", cursor="sailboat")
#btn3.pack()
btn3.grid(column=1,row=0)
#from Tkinter import ttk
#ttk.Button(root, text="Hello World").grid() #Cria botão
root.mainloop()                               #inicializa o loop