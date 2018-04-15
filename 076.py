#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 15, 2018, 4:45 AM
 * Software: PyCharm
 * Project Name: Tutorial
题目：编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n
"""


def printAl(start, N):
    count = 0
    sum = 0
    for x in range(start, N + 1, 2):
        sum += 1 / x
        if x != N:
            print(("1/%s" % x), end=' + ')
        else:
            print(("1/%s" % x), end=' = ')
    print("%s." % sum)


while True:
    N = int(input("A number: "))
    if N % 2 == 0:
        printAl(2, N)
    else:
        printAl(1, N)
