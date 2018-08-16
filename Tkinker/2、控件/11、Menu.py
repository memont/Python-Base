#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/8/16 下午9:14
# @Author : Memont# @Site : 
# @File : 11、Menu.py
# @Software: PyCharm

import tkinter

win = tkinter.Tk()
win.title("Tkinter")
win.geometry("400x400+200+200")

'''
菜单控件
'''

# 菜单条 顶层
menubarTop = tkinter.Menu(win)
win.config(menu=menubarTop)


def fun():
    print("*****")


# 创建一个菜单选项
menu1 = tkinter.Menu(menubarTop, tearoff=False)
menu1str = [str(x) for x in range(8)]
menu1str.append("quit")

# 给菜单选项添加内容
for item in menu1str:
    # print(item)
    if item == 'quit':
        # 添加分隔线
        menu1.add_separator()
        menu1.add_command(label=item, command=win.quit)
    else:
        menu1.add_command(label=item, command=fun)

# 向菜单条添加菜单
menubarTop.add_cascade(label='menu', menu=menu1)

menu2 = tkinter.Menu(menubarTop, tearoff=False)
menu2.add_command(label="a");
menu2.add_command(label="b");
menu2.add_command(label="c");
menubarTop.add_cascade(label='alpha', menu=menu2)

# 菜单 鼠标右键

menubarRight = tkinter.Menu(win)
menuRight = tkinter.Menu(menubarRight, tearoff=False)
for item in menu1str:
    menuRight.add_command(label=item)

menubarRight.add_cascade(label='right', menu=menuRight)

def showMenu(event):
    # print(event.x_root, event.y_root)
    menubarRight.post(event.x_root, event.y_root)

# 绑定鼠标右键
win.bind('<Button-3>', showMenu)


# 进入消息循环
win.mainloop()
