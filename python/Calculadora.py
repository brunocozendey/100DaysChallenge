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
        self.lblC = Tkinter.Label(self, text="Graus Centígrados")
        self.lblC.grid(column=0,row=0)
        self.lblSep= Tkinter.Label(self, text="<-->")
        self.lblSep.grid(column=1, row=0)          
        self.entryC = Tkinter.Entry(self)           
        self.entryC.grid(column=0,row=1,sticky='EW')
        self.btnCalculaF = Tkinter.Button(self,text=u"Centígrado -> Fahrenheit",command=self.OnButtonCalculaFClick)
        self.btnCalculaF.grid(column=0,row=3) 

    def OnButtonCalculaFClick(self):    
            #fCent= float(self.entryC.get())
            #fFar= (9.0 * fCent )/5 + 32.0 
            self.entryC.delete(0,Tkinter.END)
            self.entryC.insert(0,str(99))

if __name__ == "__main__":
    app = App(None)
    app.title("Conversor C<>F")
    app.mainloop()