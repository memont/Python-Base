#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/8/16 上午12:51
# @Author : Memont# @Site : 
# @File : 9、Scale.py
# @Software: PyCharm

import tkinter


win = tkinter.Tk()
win.title("Tkinter")
win.geometry("400x400+200+200")

'''
拖拽改变值 可以水平也可以竖直
orient:  HORIZONTAL 水平
         VERTICAL   竖直

length   水平表示宽度 竖直表示高度
tickinterval  标尺间隔
'''

scale = tkinter.Scale(win, from_=0, to=100, orient=tkinter.HORIZONTAL, tickinterval=20, length=200)

scale.pack()

# 设置值
scale.set(20)

# 取值
print(scale.get())

tkinter.Button(win, text='cat', command=lambda :print(scale.get())).pack()

# 进入消息循环
win.mainloop()