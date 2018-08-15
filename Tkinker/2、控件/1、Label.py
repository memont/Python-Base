#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/14 下午11:44
# @Author  : Memont
# @Email   : 18392644994@163.com 
# @Site    : 
# @File    : 1、Label.py
# @Software:


import tkinter

# 创建主窗口
win = tkinter.Tk()
# 设置标题
win.title("Tkinter")
# 设置大小和位置
win.geometry("400x400+200+200")

'''
Lable: 标签控件 可以显示文本

参数：   win       父窗体
        text      显示文本
        bg        背景色
        fg        字体色
        font      字体
        width     宽
        height    高
        wraplength 指定换行宽度
        justify    指定换行后对齐方式
        anchor     位置 n s w e nw ne sw se center
'''

lable = tkinter.Label(win,
                      text='hello world',
                      bg='blue',
                      fg='red',
                      font=('song', 16),
                      width=100,
                      height=2,
                      wraplength=40,
                      justify='left',
                      anchor='center'
                      )


lable.pack()

# 进入消息循环
win.mainloop()
