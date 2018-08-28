#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'memont'
# Email   :
# File    :4、分布式进程.py
# Datetime:2018/8/28 14:53
# Project :Python-Base

import argparse
import random
import time
import queue
import threading
from multiprocessing.managers import BaseManager


def get_run_type():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-m", "--master", help="The master", action="store_true")
    group.add_argument("-w", "--worker", help="The worker", action="store_true")
    args = parser.parse_args()
    operation = 'worker' if args.worker else 'master'
    return operation


# task_master

# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass


task_queue = queue.Queue()
result_queue = queue.Queue()


class Master(object):
    def __init__(self):
        # 发送任务的队列:
        self.task = None
        self.result = None
        self.thread = None
        self.running = False
        # self.task_queue = queue.Queue()
        # 接收结果的队列:
        # self.result_queue = queue.Queue()
        # 把两个Queue都注册到网络上, callable参数关联了Queue对象:
        # QueueManager.register('get_task_queue', callable=lambda: self.task_queue)
        QueueManager.register('get_task_queue', callable=self.return_task_queue)
        QueueManager.register('get_result_queue', callable=self.return_result_queue)
        # 绑定端口5000, 设置验证码'abc':
        self.manager = QueueManager(address=('192.168.1.13', 5000), authkey=b'abc')
        print(self.manager)

    def loop(self):
        print('Try get results...')
        while self.running:
            r = self.result.get(timeout=10)
            print('Result: %s' % r)

    def start(self):
        self.running = True
        # 启动Queue:
        self.manager.start()
        self.task = self.manager.get_task_queue()
        self.result = self.manager.get_result_queue()
        self.thread = threading.Thread(target=self.loop, name='LoopThread')
        self.thread.start()
        # 放几个任务进去:
        while self.running:
            n = random.randint(0, 10000)
            print('Put task %d...' % n)
            self.task.put(n)
            time.sleep(random.random())

    def stop(self):
        # 关闭:
        self.running = False
        self.manager.shutdown()
        print('master exit.')

    def return_task_queue(self):
        global task_queue
        return task_queue

    def return_result_queue(self):
        global result_queue
        return result_queue


# task_worker
class Worker(object):
    def __init__(self):
        # 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字:
        QueueManager.register('get_task_queue')
        QueueManager.register('get_result_queue')
        # 连接到服务器，也就是运行task_master.py的机器:
        server_addr = '192.168.1.33'
        # server_addr = '127.0.0.1'
        print('Connect to server %s...' % server_addr)
        # 端口和验证码注意保持与task_master.py设置的完全一致:
        self.m = QueueManager(address=(server_addr, 5000), authkey=b'abc')
        # 从网络连接:
        self.m.connect()

    def start(self):
        # 获取Queue的对象:
        task = self.m.get_task_queue()
        result = self.m.get_result_queue()
        # 从task队列取任务,并把结果写入result队列:
        for i in range(10):
            try:
                n = task.get(timeout=1)
                print('run task %d * %d...' % (n, n))
                r = '%d * %d = %d' % (n, n, n * n)
                time.sleep(1)
                result.put(r)
            except queue.Queue.Empty:
                print('task queue is empty.')
        # 处理结束:
        print('worker exit.')


if __name__ == '__main__':
    run_type = get_run_type()
    if run_type == 'master':
        master = Master()
        master.start()
    else:
        worker = Worker()
        worker.start()
