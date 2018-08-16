#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/8/16 下午11:39
# @Author : Memont# @Site : 
# @File : 13、Frame.py
# @Software: PyCharm

import tkinter


win = tkinter.Tk()
win.title("Tkinter")
win.geometry("400x400+200+200")

'''
框架控件
在屏幕上显示一个矩形区域， 多作为容器控件
'''

# 创建
frame = tkinter.Frame(win).pack()

# left
frame_left = tkinter.Frame(frame);
tkinter.Label(frame_left, text='左上', bg='pink').pack(side=tkinter.TOP)
tkinter.Label(frame_left, text='左下', bg='blue').pack(side=tkinter.TOP)
frame_left.pack(side=tkinter.LEFT)

# Right
frame_right = tkinter.Frame(frame);
tkinter.Label(frame_right, text='右上', bg='pink').pack(side=tkinter.TOP)
tkinter.Label(frame_right, text='右下', bg='blue').pack(side=tkinter.TOP)
frame_right.pack(side=tkinter.RIGHT)



# 进入消息循环
win.mainloop()