#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 15, 2018, 5:36 AM
 * Software: PyCharm
 * Project Name: Tutorial
题目：输入一个奇数，然后判断最少几个 9 除于该数的结果为整数。
程序分析：999999 / 13 = 76923。
"""

while True:
    N = int(input("Input an odd number: "))

    if N % 2 == 1:
        base = 1
        TEN = 10
        result = 0
        for x in range(1, 100):
            result += 9 * base
            base *= TEN
            if result % N == 0:
                print("%s / %s = %s." % (result, N, 0))
                break
