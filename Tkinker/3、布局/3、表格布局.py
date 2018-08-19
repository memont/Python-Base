#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/8/18 下午10:39
# @Author : Memont# @Site : 
# @File : 3、表格布局.py
# @Software: PyCharm


import tkinter

win = tkinter.Tk()
win.title("Tkinter")
win.geometry("400x400+200+200")

label1 = tkinter.Label(win, text='1111', bg='blue')
label2 = tkinter.Label(win, text='2222', bg='pink')
label3 = tkinter.Label(win, text='3333', bg='red')
label4 = tkinter.Label(win, text='4444', bg='yellow')

# 表格布局
label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=1, column=0)
label4.grid(row=1, column=1)

# 进入消息循环
win.mainloop()
