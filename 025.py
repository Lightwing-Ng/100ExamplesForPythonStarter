#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 14, 2018, 11:04 PM
 * Software: PyCharm
 * Project Name: Tutorial
题目：求1+2!+3!+...+20!的和。
程序分析：此程序只是把累加变成了累乘。
"""


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


while True:
    N = int(input("The Number: "))
    sum = 0
    for i in range(1, N + 1):
        sum += factorial(i)
        if i != N:
            print(("%s!" % i), end=' + ')
        else:
            print(("%s!" % i), end=' = ')

    print(format(sum, ','), end='.\n')
