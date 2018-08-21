#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'memont'
# Email   :
# File    :2、reduce.py
# Datetime:2018/8/21 16:36
# Project :Python-Base

# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，
# reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

# 对一个序列求和，就可以用reduce实现：

from functools import reduce


def add(x, y):
    return x + y


print(reduce(add, [1, 2, 3, 4]))

print(sum([1, 2, 3, 4]))


# 配合map()，我们就可以写出把str转换为int的函数：

def char2num(c):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[c]


def f(x, y):
    return 10 * x + y


print(reduce(f, map(char2num, '11236675756')))


# 整理成一个str2int的函数就是：
def str2int(s):
    def f(x, y):
        return 10 * x + y

    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

    return reduce(f, map(char2num, s))


print(str2int('123456789'))

# 还可以用lambda函数进一步简化成：
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def char2num(s):
    return DIGITS[s]


def str3int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


print('123456789')
