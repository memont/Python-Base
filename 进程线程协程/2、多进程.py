#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'memont'
# Email   :
# File    :2、多进程.py
# Datetime:2018/8/28 10:38
# Project :Python-Base

from multiprocessing import Process
from multiprocessing import Pool
from multiprocessing import Queue

import os
import random
import time
import subprocess

'''
multiprocessing 跨平台版本的多进程模块
Process类来代表一个进程对象
'''


# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


def strat_proc():
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()  # start()方法启动
    p.join()  # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
    print('Child process end.')


'''
Pool 进程池 批量创建子进程：
'''


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


'''
apply 阻塞 等待当前子进程执行完毕后，在执行下一个进程
apply_async 异步非阻塞 不用等待当前进程执行完毕，随时根据系统调度来进行进程切换
'''


def start_pool():
    p = Pool()  # Pool的默认大小是CPU的核数
    for i in range(8):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')


'''
subprocess 模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出
'''


def start_subprocess():
    '''
    print('$ nslookup www.python.org')
    r = subprocess.call(['nslookup', 'www.python.org'])
    print('Exit code:', r)
    '''
    print('$ nslookup')
    p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
    print(output.decode('gbk'))
    print('Exit code:', p.returncode)


# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())


# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)


def start_process_queue():
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()


if __name__ == '__main__':
    # strat_proc()
    # start_pool()
    # start_subprocess()
    start_process_queue()
