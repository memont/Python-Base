#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/8/16 上午1:03
# @Author : Memont# @Site : 
# @File : 10、Spinbox.py
# @Software: PyCharm

import tkinter


win = tkinter.Tk()
win.title("Tkinter")
win.geometry("400x400+200+200")

'''
数值范围控件
increment 步长 默认 1
values    指定值范围 和 from_ to 不一起用
'''

def update():
    print(v.get())

v = tkinter.StringVar()

sp = tkinter.Spinbox(win, from_=0, to=100, increment=10, textvariable=v, command=update)
# sp = tkinter.Spinbox(win, increment=10, values=(0, 2, 4, 6, 8))
sp.pack()

# 设置值
v.set(40)

# 取值
print(v.get())

# 进入消息循环
win.mainloop()