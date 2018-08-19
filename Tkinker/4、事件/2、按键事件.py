#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/8/18 下午11:48
# @Author : Memont# @Site : 
# @File : 2、按键事件.py
# @Software: PyCharm


import tkinter

win = tkinter.Tk()
win.title("Tkinter")
win.geometry("400x400+200+200")


'''
按键事件
<Key> 响应所有的按键 (控件绑定需要focus_set win不需要）

特殊按键
<Shift_L>
<Shift_R>
<F5>
<Return>  回车
<BackSpace>

指定按键事件
a 1 

组合按键事件
<Control-Alt-Up>

'''

def fun(event):
    print(event)


lable = tkinter.Label(win, text='key event')
# 设置焦点
lable.focus_set()
lable.bind('<Control-1>', fun)

lable.pack();

# win.bind('<Key>', fun)

# 进入消息循环
win.mainloop()
