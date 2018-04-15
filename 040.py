#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 15, 2018, 1:28 AM
 * Software: PyCharm
 * Project Name: Tutorial
"""

import random

while True:
    N = int(input("The length of List: "))
    L = [random.randint(10, 100) for x in range(N)]
    print(L)

    for i in range(int(N / 2)):
        L[i], L[N - i - 1] = L[N - i - 1], L[i]

    print(L)
