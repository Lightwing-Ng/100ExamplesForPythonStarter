#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 15, 2018, 4:11 AM
 * Software: PyCharm
 * Project Name: Tutorial
题目：有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。
程序分析：无。
"""

while True:
    N = int(input("Number of People: "))
    L = []
    for x in range(1, N + 1):
        L.append(x)
    print(L)

    while len(L) > 2:
        PeopleQuit = L[2::3]
        for x in PeopleQuit:
            L.remove(x)
        print(L)