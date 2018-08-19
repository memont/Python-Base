#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/8/18 下午10:43
# @Author : Memont# @Site : 
# @File : 1、鼠标事件.py
# @Software: PyCharm


import tkinter

win = tkinter.Tk()
win.title("Tkinter")
win.geometry("400x400+200+200")

'''
鼠标点击事件
<Button-i>  鼠标Button-1(左), Button-2(中), Button-3(右)， 当在控件上单击左键时，Tkinter会自动抓取到鼠标指针的位置，
            ButtonPressed-i是Button-i的代名词

<Double-Button-i> 双击
<Triple-Button-i> 三击

鼠标释放事件
<ButtonRelease-i> i(1, 2, 3)


鼠标移动事件
<Bi-Motion> 按下鼠标(i 1 2 3)键并在小构件内移动时事件发生
<Enter> 鼠标进入时事件发生
<Leave> 鼠标离开时事件发生



'''

'''
event 产生的事件对象 

'''

'''
x, y 为相对于控件的位置， x_root, y_root 则为相对于屏幕
'''


def fun(event):
    # print(event.x, event.y, event.x_root, event.y_root)
    print(event)
    button1['bg'] = 'red'



def enter(event):
    print(event)
    label['bg'] = 'red'


def leave(event):
    print(event)
    label['bg'] = 'white'


button1 = tkinter.Button(win, text='left mouse button')
label = tkinter.Label(win, text='left mouse label')

# bind 给控件绑定事件

# button1.bind('<Button-1>', fun)
# button1.bind('<Double-Button-1>', fun)
# button1.bind('<B1-Motion>', fun)
# button1.bind('<Triple-Button-1>', fun)
# button1.bind('<ButtonRelease-1>',fun)

button1.bind('<Key>', fun)

label.bind('<Enter>', enter)
label.bind('<Leave>', leave)

button1.pack()
label.pack()

# 进入消息循环
win.mainloop()
