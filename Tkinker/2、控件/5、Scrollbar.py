#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/8/15 下午11:33
# @Author : Memont# @Site : 
# @File : 5、Scrollbar.py
# @Software: PyCharm


import tkinter


win = tkinter.Tk()
win.title("Tkinter")
# win.geometry("400x400+200+200")

# 创建滚动条
scroll = tkinter.Scrollbar(win)
text = tkinter.Text(win, width=50, height=4)

# side 窗体的那一侧
# fill 填充
scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)
text.pack(side=tkinter.LEFT, fill=tkinter.Y)

# 关联
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)


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


# 进入消息循环
win.mainloop()