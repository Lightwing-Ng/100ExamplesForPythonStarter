#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 15, 2018, 2:18 AM
 * Software: PyCharm
 * Project Name: Tutorial
题目：两个变量值互换。
程序分析：无
"""
import random

def exchange(a, b):
    a, b = b, a
    return (a, b)


if __name__ == '__main__':
    x = random.randint(10, 100)
    y = random.randint(10, 100)
    print('x = %d, y = %d' % (x, y))

    x, y = exchange(x, y)
    print('x = %d, y = %d' % (x, y))
