#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/8/15 下午11:43
# @Author : Memont# @Site : 
# @File : 6、Checkbutton.py
# @Software: PyCharm

import tkinter


win = tkinter.Tk()
win.title("Tkinter")
win.geometry("400x400+200+200")

def update():
    message = ''
    if hobby1.get() == True:
        message += 'A '
    if hobby2.get() == True:
        message += 'B '
    if hobby3.get() == True:
        message += 'C '
    text.delete(0.0, tkinter.END)
    text.insert(tkinter.INSERT, message)

'''
复选框
'''

hobby1 = tkinter.BooleanVar()
hobby2 = tkinter.BooleanVar()
hobby3 = tkinter.BooleanVar()

check1 = tkinter.Checkbutton(win, text='A', variable=hobby1, command=update).pack()
check2 = tkinter.Checkbutton(win, text='B', variable=hobby2, command=update).pack()
check3 = tkinter.Checkbutton(win, text='C', variable=hobby3, command=update).pack()

text = tkinter.Text(win, width=40, height=4)
text.pack()

# 进入消息循环
win.mainloop()