#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 15, 2018, 4:41 AM
 * Software: PyCharm
 * Project Name: Tutorial
题目：列表排序及连接。
程序分析：排序可使用 sort() 方法，连接可以使用 + 号或 extend() 方法。
"""

import random

while True:
    N = int(input("Length: "))
    a = [random.randint(10, 100) for x in range(N)]
    b = [random.randint(10, 100) for x in range(N)]

    a.sort()  # 对列表 a 进行排序
    print(a)

    # 连接列表 a 与 b
    print(a + b)

    # 连接列表 a 与 b
    a.extend(b)
    print(a)
