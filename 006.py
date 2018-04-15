#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 14, 2018, 6:41 PM
 * Software: PyCharm
 * Project Name: Tutorial
题目：斐波那契数列。
程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
在数学上，费波那契数列是以递归的方法来定义
"""


def fib_1(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib_1(n - 1) + fib_1(n - 2)


print(fib_1(10))
