#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 14, 2018, 8:00 PM
 * Software: PyCharm
 * Project Name: Tutorial
题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
程序分析：兔子的规律为数列1,1,2,3,5,8,13,21....
"""

a = 1
b = 1

for i in range(1, 22):
    print("%12ld, %12ld" % (a, b))
    a = a + b
    b = a + b
