# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 16:31:30 2015

@author: xinyan wang
"""

from tkinter import *
root = Tk()
#左对齐，文本居中
Label(root,text = 'welcome to jcodeer.cublog.cn',bg = 'yellow',width = 40,
      height = 3,wraplength = 80,justify = 'left').pack()
#居中对齐，文本居左
Label(root,text = 'welcome to jcodeer.cublog.cn',bg = 'red',width = 40,
      height = 3,wraplength = 80,anchor = 'w').pack()
#居中对齐，文本居右
Label(root,text = 'welcome to jcodeer.cublog.cn',bg = 'blue',width = 40,
      height = 3,wraplength = 80,anchor = 'e').pack()

root.mainloop()