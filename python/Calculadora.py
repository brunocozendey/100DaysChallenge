#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import * 
class App(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()
    
    def initialize(self):
        self.grid()
        self.lblC = Tkinter.Label(self, text="Graus Centígrados")
        self.lblC.grid(column=0,row=0)

if __name__ == "__main__":
    app = App(None)
    app.title("Conversor C<>F")
    app.mainloop()