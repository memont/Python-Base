#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/8/15 下午10:38
# @Author : Memont# @Site : 
# @File : 2、Button.py
# @Software: PyCharm

import tkinter


def func():
    print('on click')


win = tkinter.Tk()
win.title("Tkinter")
win.geometry("400x400+200+200")

# 创建按钮
button = tkinter.Button(win, text='button', command=func, width=10, height=2)
button.pack()
# 匿名函数
button1 = tkinter.Button(win, text='lambda', command=lambda: print('on click lambda'))
button1.pack()
# 匿名函数
button2 = tkinter.Button(win, text='quit', command=win.quit)
button2.pack()

# 进入消息循环
win.mainloop()
