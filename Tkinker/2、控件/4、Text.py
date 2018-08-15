#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/8/15 下午11:23
# @Author : Memont# @Site : 
# @File : 4、Text.py
# @Software: PyCharm

import tkinter


win = tkinter.Tk()
win.title("Tkinter")
win.geometry("400x400+200+200")

'''
文本控件 用于显示多航文本
width  宽度
height 行数
'''
text = tkinter.Text(win, width=40, height=4)
text.pack()

str = '''⌃Space 基本的代码补全（补全任何类、方法、变量）
⌃⇧Space 智能代码补全（过滤器方法列表和变量的预期类型）
⌘⇧↩ 自动结束代码，行末自动添加分号
⌘P 显示方法的参数信息
⌃J, Mid. button click 快速查看文档
⇧F1 查看外部文档（在某些代码上会触发打开浏览器显示相关文档）
⌘+鼠标放在代码上 显示代码简要信息

作者：神SKY
链接：https://www.jianshu.com/p/82cdc0eddb16
來源：简书
简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。
'''

text.insert(tkinter.INSERT, str)
# text.delete(0.0, tkinter.END)

# 进入消息循环
win.mainloop()