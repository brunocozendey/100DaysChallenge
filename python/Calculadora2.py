#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *

root = Tk()             #cria a aplicação raiz. 

menubar = Menu(root)
root.config(menu=menubar)

root.title(string="..:: CALCULADORA ::..")


filemenu = Menu(menubar)
menubar.add_cascade(label='Arquivo', menu=filemenu)
filemenu.add_command(label='Sair', command=root.destroy)

frame1 = Frame(root)
#frame1.pack(side=TOP, fill=X)
frame1.grid()

frame2 = Frame(root)
#frame2.pack(side=RIGHT, fill=X)
frame2.grid()

frame3 = Frame(root)
frame3.grid()

'''
submenu=Menu(mainmenu)
mainmenu.add_cascade(label='File',menu=submenu)
submenu.add_command(label='Open', command=donothing)
submenu.add_separator()
submenu.add_command(label='Exit', command=frame1.quit)        
'''     
titulo = Label(frame1, text="Resultado:")
titulo.grid(column=0,row=0)          
entrada = Entry(frame1) 
entrada.insert(0,str(0))          
entrada.grid(column=0,row=1,sticky='EW')
btnUm = Button(frame2,text="1",command= lambda:OnButtonNumClick(1))
btnUm.grid(column=3,row=4)
btnDois = Button(frame2,text="2",command=lambda:OnButtonNumClick(2))
btnDois.grid(column=2,row=4) 
btnTres = Button(frame2,text="3",command=lambda:OnButtonNumClick(3))
btnTres.grid(column=1,row=4) 
btnQuatro = Button(frame2,text="4",command=lambda:OnButtonNumClick(4))
btnQuatro.grid(column=3,row=3)
btnCinco = Button(frame2,text="5",command=lambda:OnButtonNumClick(5))
btnCinco.grid(column=2,row=3)
btnSeis = Button(frame2,text="6",command=lambda:OnButtonNumClick(6))
btnSeis.grid(column=1,row=3)
btnSete = Button(frame2,text="7",command=lambda:OnButtonNumClick(7))
btnSete.grid(column=3,row=2)
btnOito = Button(frame2,text="8",command=lambda:OnButtonNumClick(8))
btnOito.grid(column=2,row=2)
btnNove = Button(frame2,text="9",command=lambda:OnButtonNumClick(9))
btnNove.grid(column=1,row=2)
btnZero = Button(frame2,text="0",command=lambda:OnButtonNumClick(0))
btnZero.grid(column=2,row=5)

btnSoma = Button(frame2, text=".", command=lambda:OnButtonOperClick("."))
btnSoma.grid(column=1, row=5)

btnSoma = Button(frame2, text="+", command=lambda:OnButtonOperClick("+"))
btnSoma.grid(column=2, row=6)
btnSubtracao = Button(frame2, text="-", command=lambda:OnButtonOperClick("-"))
btnSubtracao.grid(column=3, row=6)

btnSubtracao = Button(frame2, text="*", command=lambda:OnButtonOperClick("*"))
btnSubtracao.grid(column=2, row=7)

btnSubtracao = Button(frame2, text="/", command=lambda:OnButtonOperClick("/"))
btnSubtracao.grid(column=3, row=7)

btnIgual = Button(frame2, text=")", command=lambda:OnButtonNumClick(")"))
btnIgual.grid(column=1, row=7)

btnIgual = Button(frame2, text="(", command=lambda:OnButtonNumClick("("))
btnIgual.grid(column=1, row=6)

btnIgual = Button(frame2, text="=", command=lambda:OnButtonIgualClick())
btnIgual.grid(column=3, row=5)

btnClr = Button(frame1, text="CLR", command=lambda:OnButtonClrClick())
btnClr.grid(column=0, row=2)

btnBksp = Button(frame1, text="<-", command=lambda:OnButtonBkspClick())
btnBksp.grid(column=1, row=2)

#btnSair = Button(frame2, text="Sair", fg ="gray", bg="red", command=root.destroy)
#btnSair.grid(column=0, row=8)
        
def OnButtonNumClick(n):    
    value =entrada.get()
    if value.isdigit():
        if n == 0:
            if (value[-1] in ["+","-","/","*","."]): # para remover o zero a esquerda
                entrada.delete(0,END)
                entrada.insert(END,str(value))
            else:
                entrada.insert(END,str(n))
            
        else:    
            if int(value) == 0:
                entrada.delete(0,END)
                entrada.insert(END,str(n))
            else:
                entrada.insert(END,str(n))
    else:
        entrada.insert(END,str(n))

        
def OnButtonIgualClick():
    a =entrada.get()
    entrada.delete(0,END)
    try:
        entrada.insert(0,eval(a)) #eval() resolve qualquer tipo de equação.
    except:
        entrada.insert(0,"Err")
        
def OnButtonBkspClick():
    value =entrada.get()
    if len(value) == 1:
        entrada.delete(0,END)
        entrada.insert(0,str(0))
    else:
        entrada.delete(0,END)
        entrada.insert(0,value[:-1])

def OnButtonClrClick():
    entrada.delete(0,END)
    entrada.insert(0,str(0))

def OnButtonOperClick(operador):
    value =entrada.get()
    if (value[-1] in ["+","-","/","*","."]):
        entrada.delete(0,END)
        entrada.insert(0,value)
    else:
        entrada.insert(END,operador)

root.mainloop()