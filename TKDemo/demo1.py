# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 15:35:39 2015

@author: xinyan wang

TKDemo1 for BioChem repeating.
"""
import inspect,os
import tkinter as Tkinter

def getplace():
    this_file=inspect.getfile(inspect.currentframe())  
    path=os.path.abspath(os.path.dirname(this_file))  
    return path


def main():    
    root=Tkinter.Tk()
    root.title('AA')
    im=Tkinter.PhotoImage(file='%s\\pic\\alanine.gif'%getplace())
    label=Tkinter.Label(root,image=im,text='image',compound='top')
    label.pack()
    root.mainloop()
    
if __name__=='__main__':
    main()