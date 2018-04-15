#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 15, 2018, 1:15 AM
 * Software: PyCharm
 * Project Name: Tutorial

题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
程序分析：首先判断此数是否大于最后一个数，然后再考虑插入中间的数的情况，插入后此元素之后的数，依次后移一个位置。
"""

import random

while True:
    N = int(input("Type the length of the List: "))
    L = []
    for i in range(N):
        L.append(random.randint(10, 100))
    L.sort()
    print(L)
    key = int(input("Type a number to insert: "))
    L.append(key)
    L.sort()
    print(L)
