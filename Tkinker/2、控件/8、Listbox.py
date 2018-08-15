#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/8/16 上午12:03
# @Author : Memont# @Site : 
# @File : 8、Listbox.py
# @Software: PyCharm

import tkinter

win = tkinter.Tk()
win.title("Tkinter")
# win.geometry("400x400+200+200")

'''
列表框控件， 可以包含一个或多个文本框
作用： 在listbox控件小窗口显示一个字符串
'''

# 1创建 添加元素

# SINGLE  和BROWSE相似，但是不支持鼠标按下后移动选中位置
# BROWSE
# EXTENDED 使lixtbox 指出shift 和 cotrol
# MULTIPLE 支持多选

# 绑定变量
lbv = tkinter.StringVar()

lb = tkinter.Listbox(win, selectmode=tkinter.MULTIPLE, listvariable=lbv)
# lb.pack()

for item in ['1', '2', '3', '4', '5']:
    #   按顺序添加
    lb.insert(tkinter.END, item)
# 在开始添加
lb.insert(tkinter.ACTIVE, '0')

# 将列表当作一个元素添加
lb.insert(tkinter.END, ['a', 'b', 'c'])

# 删除 参数1 开始的索引，
#      参数2 结束的索引 缺省只删除一个
# lb.delete(1, 3)
lb.delete(1)

# 选中 参数1 开始的索引，
#     参数2 结束的索引 缺省只选中一个
lb.select_set(2, 4)
lb.select_set(0)
# 取消选中
lb.select_clear(2, 3)

# 获取列表中元素的个数
print(lb.size())

# 从列表取值 参数1 开始的索引，
#          参数2 结束的索引 缺省获取一个
print(lb.get(2, 4))
print(lb.get(0))

# 返回当前选中索引
print(lb.curselection())

# 判断某个元素是否被选中
print(lb.select_includes(1))
print(lb.select_includes(0))

print(lbv.get())
lbv.set(('z', 'x', 'c', 'v', 'b', 'n', 'm', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k'))


# 绑定事件
def myPrint(event):
    print(lb.get(lb.curselection()))


lb.bind('<Double-Button-1>', myPrint)

# 滚动条
sc = tkinter.Scrollbar(win)
sc.pack(side=tkinter.RIGHT, fill=tkinter.Y)
lb.configure(yscrollcommand=sc.set)
lb.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
sc['command'] = lb.yview

# 进入消息循环
win.mainloop()
