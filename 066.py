#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 15, 2018, 3:45 AM
 * Software: PyCharm
 * Project Name: Tutorial
题目：输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。
程序分析：无。
"""

import random, numpy

while True:
    N = int(input("The length of List: "))
    L = []
    for x in range(N):
        L.append(random.randint(10, 100))
    print(L)

    L[L.index(max(L))], L[0] = L[0], L[L.index(max(L))]
    L[L.index(min(L))], L[N - 1] = L[N - 1], L[L.index(min(L))]

    print(L, "\n")
