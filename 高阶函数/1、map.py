#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'memont'

# Email   :
# File    :1、map.py
# Datetime:2018/8/21 15:57
# Project :Python-Base

import time


# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。

def f(x):
    return x * x


start = time.clock()
print(list(map(f, [1, 2, 3, 4, 5])))

# map()传入的第一个参数是f 函数，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。

# 把这个list所有数字转为字符串：

print(list(map(str, [1, 2, 3, 4, 5])))
print("time:", time.clock() - start)
