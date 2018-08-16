#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/8/16 下午11:03
# @Author : Memont# @Site : 
# @File : 12、Combobox.py
# @Software: PyCharm

import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.title("Tkinter")
win.geometry("400x400+200+200")

'''
下拉控件
'''


# 绑定变量
cv = tkinter.StringVar()
# 创建下来控件
com = ttk.Combobox(win, textvariable=cv)
com.pack()

# 设置下拉数据
com['value'] = ('1', '2', '3')

# 设置默认值
com.current(0)


def comSelected(event):
    print(com.get())
    print(cv.get())


# 绑定事件
com.bind('<<ComboboxSelected>>', comSelected)

# 进入消息循环
win.mainloop()

