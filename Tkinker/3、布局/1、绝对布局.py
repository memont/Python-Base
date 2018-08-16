#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/8/17 上午12:50
# @Author : Memont# @Site : 
# @File : 1、绝对布局.py
# @Software: PyCharm

import tkinter


win = tkinter.Tk()
win.title("Tkinter")
win.geometry("400x400+200+200")


label1 = tkinter.Label(win, text='1111')
label2 = tkinter.Label(win, text='2222')
label3 = tkinter.Label(win, text='3333')
label4 = tkinter.Label(win, text='4444')

# 绝对布局， 窗口的变化对位置没有影响
label1.place(x=10, y=20)
label2.place(x=30, y=40)
label3.place(x=60, y=60)
label4.place(x=100, y=80)


# 进入消息循环
win.mainloop()