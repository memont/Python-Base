#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/8/18 下午10:32
# @Author : Memont# @Site : 
# @File : 2、相对布局.py
# @Software: PyCharm


import tkinter


win = tkinter.Tk()
win.title("Tkinter")
win.geometry("400x400+200+200")

label1 = tkinter.Label(win, text='1111', bg='blue')
label2 = tkinter.Label(win, text='2222', bg='pink')
label3 = tkinter.Label(win, text='3333', bg='red')
label4 = tkinter.Label(win, text='4444', bg='yellow')


# 相对布局， 窗体改变对控件有影响
label1.pack(fill=tkinter.Y, side=tkinter.LEFT);
label2.pack(fill=tkinter.X, side=tkinter.TOP);
label3.pack(fill=tkinter.X, side=tkinter.BOTTOM);
label4.pack()


# 进入消息循环
win.mainloop()

