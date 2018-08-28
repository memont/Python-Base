#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'memont'
# Email   :
# File    :3、多线程.py
# Datetime:2018/8/28 11:29
# Project :Python-Base

import threading
import time

'''
启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行：
由于任何进程默认就会启动一个线程，我们把该线程称为主线程，主线程又可以启动新的线程，
Python的threading模块有个current_thread()函数，它永远返回当前线程的实例。
主线程实例的名字叫MainThread，子线程的名字在创建时指定，我们用LoopThread命名子线程。
名字仅仅在打印时用来显示，完全没有其他意义，如果不起名字Python就自动给线程命名为Thread-1，Thread-2……
'''


# 新线程执行的代码:
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


def start_thread():
    print('thread %s is running...' % threading.current_thread().name)
    t = threading.Thread(target=loop, name='LoopThread')
    t.start()
    t.join()
    print('thread %s ended.' % threading.current_thread().name)


'''
Lock: 
'''
# 假定这是你的银行存款:
balance = 0
lock = threading.Lock()


def change_it(n):
    # 先存后取，结果应该为0:
    lock.acquire()
    global balance
    balance = balance + n
    balance = balance - n
    lock.release()


def run_thread(n):
    for i in range(1000000):
        change_it(n)


def start_thread_unlock():
    t1 = threading.Thread(target=run_thread, args=(5,))
    t2 = threading.Thread(target=run_thread, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)


'''
ThreadLocal 
'''

# 创建全局ThreadLocal对象:
local_school = threading.local()


def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))


def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()


def start_thread_local():
    t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
    t2 = threading.Thread(target=process_thread, args=('Bob', ), name='Thread-B')
    t1.start()
    t2.start()
    t1.join()
    t2.join()


if __name__ == '__main__':
    # start_thread()
    # start_thread_unlock()
    start_thread_local()
