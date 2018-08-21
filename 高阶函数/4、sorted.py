#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'memont'
# Email   :
# File    :4、sorted.py
# Datetime:2018/8/21 17:02
# Project :Python-Base

# 排序: 冒泡 选择          数据量大时效率低下
#       快速 插入 计数器


# 普通的排序

listA = [4, -5, 2, 9, -1, 6]
# 默认升序
listR = sorted(listA)
print(listR)

# 倒叙
listR = sorted(listA, reverse=True)
print(listR)

# 排序规则 key 指定函数确定排序规则
print(sorted(listA, key=abs))
print(listA)
