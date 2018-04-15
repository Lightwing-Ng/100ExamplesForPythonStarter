#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 15, 2018, 4:02 AM
 * Software: PyCharm
 * Project Name: Tutorial
题目：有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数
程序分析：无。
"""
import random

while True:
    N = int(input("The length of List: "))
    L = [random.randint(10, 100) for x in range(N)]
    print(L)

    m = int(input("m: "))
    L[0:N - m - 1], L[N - m:N - 1] = L[N - m:N - 1], L[0:N - m - 1]
    print(L)
