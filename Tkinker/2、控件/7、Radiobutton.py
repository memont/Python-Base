#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/8/15 下午11:56
# @Author : Memont# @Site : 
# @File : 7、Radiobutton.py
# @Software: PyCharm

import tkinter


win = tkinter.Tk()
win.title("Tkinter")
win.geometry("400x400+200+200")

# 获取value
def update():
    print(r.get())

'''
单选框控件
'''


# 一组单选框绑定一个变量
r = tkinter.IntVar()
radio1 = tkinter.Radiobutton(win, text='1', value=1, variable=r, command=update).pack()
radio2 = tkinter.Radiobutton(win, text='2', value=2, variable=r, command=update).pack()
radio3 = tkinter.Radiobutton(win, text='3', value=3, variable=r, command=update).pack()
radio4 = tkinter.Radiobutton(win, text='4', value=4, variable=r, command=update).pack()


# 进入消息循环
win.mainloop()