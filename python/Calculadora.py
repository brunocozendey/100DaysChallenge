#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter
class App(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()
    
    def initialize(self):
        self.grid()
        self.titulo = Tkinter.Label(self, text="Resultado:")
        self.titulo.grid(column=0,row=0)          
        self.entrada = Tkinter.Entry(self)           
        self.entrada.grid(column=0,row=1,sticky='EW')
        self.btnUm = Tkinter.Button(self,text="1",command=self.OnButtonCalculaFClick(1))
        self.btnUm.grid(column=0,row=2)
        self.btnDois = Tkinter.Button(self,text="2",command=self.OnButtonCalculaFClick(2))
        self.btnDois.grid(column=1,row=2) 
        self.btnTres = Tkinter.Button(self,text="3",command=self.OnButtonCalculaFClick(3))
        self.btnTres.grid(column=2,row=2) 

    def OnButtonCalculaFClick(self,n):    
            #fCent= float(self.entryC.get())
            #fFar= (9.0 * fCent )/5 + 32.0 
            #self.entrada.delete(0,Tkinter.END)
            self.entrada.insert(0,str(n))
if __name__ == "__main__":
    app = App(None)
    app.title("..:: Calculadora ::..")
    app.mainloop()