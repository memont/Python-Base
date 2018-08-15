#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/8/15 下午10:54
# @Author : Memont# @Site : 
# @File : 3、Entry.py
# @Software: PyCharm

import tkinter


def showInfo():
    print('on click')

win = tkinter.Tk()
win.title("Tkinter")
win.geometry("400x400+200+200")

'''
输入控件 
用于显示简单的内容
'''

# show 密文显示
entry = tkinter.Entry(win, show='*')
entry.pack()


e = tkinter.Variable()
# 绑定变量 取输入值
entry1 = tkinter.Entry(win, textvariable=e)
entry1.pack()

# 绑定后 e 代表输入框对象
# 设置值 没有 entry.set
e.set('ting ting')

# 获取值 两种方式
print(e.get())
print(entry1.get())

button = tkinter.Button(win, text='ok', command=showInfo)
button.pack()


# 进入消息循环
win.mainloop()