#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/8/17 上午12:00
# @Author : Memont# @Site : 
# @File : 14、Treeview.py
# @Software: PyCharm


import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.title("Tkinter")
win.geometry("800x600+200+200")

# 创建
tree = ttk.Treeview(win)
tree.pack()

"""

'''
表格数据
'''

# 定义列
tree['columns'] = ("A", "B", "C", "D")



# 设置列
tree.column("A", width=100)
tree.column("B", width=100)
tree.column("C", width=100)
tree.column("D", width=100)


# 设置表头 显示
tree.heading("A", text="姓名")
tree.heading("B", text="性别")
tree.heading("C", text="年龄")
tree.heading("D", text="体重")


# 添加数据
tree.insert('', 0, text='line1', values=('A1', 'M', '23', '60kg'))
tree.insert('', 1, text='line1', values=('A2', 'F', '23', '65kg'))
"""

'''
树状结构
'''
# 一级树状
treeF1 = tree.insert('', 0, '中国', text='中国ZH', values=('F0',))
treeF2 = tree.insert('', 1, '美国', text='美国USA', values=('F1',))
treeF3 = tree.insert('', 2, '英国', text='英国EN', values=('F2',))

# 二级树枝
treeF1_1 = tree.insert(treeF1, 0, '黑龙江', text='黑龙江', values=('F1_1',))
treeF1_2 = tree.insert(treeF1, 1, '吉林', text='吉林', values=('F1_2',))
treeF1_3 = tree.insert(treeF1, 2, '辽林', text='辽林', values=('F1_3',))

treeF2_1 = tree.insert(treeF2, 0, '1', text='1', values=('F2_1',))
treeF2_2 = tree.insert(treeF2, 1, '2', text='2', values=('F2_2',))
treeF2_3 = tree.insert(treeF2, 2, '3', text='3', values=('F2_3',))

treeF3_1 = tree.insert(treeF3, 0, 'A', text='A', values=('F3_1',))
treeF3_2 = tree.insert(treeF3, 1, 'B', text='B', values=('F3_2',))
treeF3_3 = tree.insert(treeF3, 2, 'C', text='C', values=('F3_3',))

# 第三个参数不能重复
# 三级树枝
treeF1_1_1 = tree.insert(treeF1_1, 0, '5', text='1')
treeF1_1_2 = tree.insert(treeF1_1, 1, '6', text='2')
treeF1_1_3 = tree.insert(treeF1_1, 2, '7', text='3')
treeF1_1_4 = tree.insert(treeF1_1, 3, '8', text='4')

# 进入消息循环
win.mainloop()
