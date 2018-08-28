#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'memont'
# Email   :
# File    :1、协程.py
# Datetime:2018/8/24 14:23
# Project :Python-Base


'''
协程，又称微线程，纤程。英文名Coroutine。
    子程序，或者称为函数，在所有语言中都是层级调用，层级返回,所以子程序调用是通过栈实现的，
一个线程就是执行一个子程序。 -->A-->B-->C     调用顺序
                                A<--B<--C<--  返回顺序    
子程序调用总是一个入口，一次返回，调用顺序是明确的。而协程的调用和子程序不同。

协程看上去也是子程序，但执行过程中，在子程序内部可中断，然后转而执行别的子程序，
在适当的时候再返回来接着执行。

注意，在一个子程序中中断，去执行其他子程序，不是函数调用，有点类似CPU的中断。比如子程序A、B：



def A():
    print('1', end=" ")
    print('2', end=" ")
    print('3', end=" ")

def B():
    print('x', end=" ")
    print('y', end=" ")
    print('z', end=" ")

假设由协程执行，在执行A的过程中，可以随时中断，去执行B，
B也可能在执行过程中中断再去执行A，结果可能是：1 2 x y 3 z
但是在A中是没有调用B的，所以协程的调用比函数调用理解起来要难一些。
看起来A、B的执行有点像多线程，但协程的特点在于是一个线程执行
    
协程比多线程优势:
    协程极高的执行效率。因为子程序切换不是线程切换，而是由程序自身控制，
因此，没有线程切换的开销，和多线程比，线程数量越多，协程的性能优势就越明显。
    第二大优势就是不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量
冲突，在协程中控制共享资源不加锁，只需要判断状态就好了，所以执行效率比多线程高很多。

因为协程是一个线程执行，那怎么利用多核CPU呢？最简单的方法是多进程+协程，既充分利用多核，
又充分发挥协程的高效率，可获得极高的性能。Python对协程的支持是通过generator实现的。
在generator中，我们不但可以通过for循环来迭代，还可以不断调用next()函数获取由yield语句返回的下一个值。

但是Python的yield不但可以返回一个值，它还可以接收调用者发出的参数
'''
'''
传统的生产者-消费者模型是一个线程写消息，一个线程取消息，
通过锁机制控制队列和等待，但一不小心就可能死锁。
如果改用协程，生产者生产消息后，直接通过yield跳转到消费者开始执行，
待消费者执行完毕后，切换回生产者继续生产，效率极高：
'''

# consumer函数是一个generator
def consumer():
    r = ''
    while True:
        # consumer通过yield拿到消息，处理，又通过yield把结果传回；
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def producer(c):
    # 首先调用c.send(None)启动生成器；
    c.send(None)
    n = 0
    while n < 10:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        # 然后，一旦生产了东西，通过c.send(n)切换到consumer执行
        r = c.send(n)
        # produce拿到consumer处理的结果，继续生产下一条消息；
        print('[PRODUCER] Consumer return: %s' % r)
    # produce决定不生产了，通过c.close()关闭consumer，整个过程结束。
    c.close()


c = consumer()

# 把一个consumer传入produce后：
producer(c)

'''
整个流程无锁，由一个线程执行，produce和consumer协作完成任务，所以称为“协程”，
而非线程的抢占式多任务。

最后套用Donald Knuth的一句话总结协程的特点：“子程序就是协程的一种特例。”
'''
