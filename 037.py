#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 15, 2018, 12:44 AM
 * Software: PyCharm
 * Project Name: Tutorial
题目：对10个数进行排序。
程序分析：可以利用选择法，即从后9个比较过程中，选择一个最小的与第一个元素交换，下次类推，即用第二个元素与后8个进行比较，并进行交换。
"""

import random

while True:
    L = []
    N = int(input("Please input the length of List: "))
    for i in range(N):
        L.append(random.randint(10, 100))

    for i in range(N):
        for j in range(i + 1, N):
            if L[i] > L[j]:
                L[i], L[j] = L[j], L[i]

    count = 0
    for i in L:
        if count != len(L) - 1:
            print(i, end=' < ')
        else:
            print(i, end='.\n')
        count += 1
