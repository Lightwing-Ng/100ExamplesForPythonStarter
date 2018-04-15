#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 15, 2018, 7:40 PM
 * Software: PyCharm
 * Project Name: Tutorial
题目：读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的＊。
程序分析：无。
"""

n = 1
while n <= 7:
    a = int(input('input a number: \n'))
    while a < 1 or a > 50:
        a = int(input('input a number: \n'))
    print(a * '-')
    n += 1
