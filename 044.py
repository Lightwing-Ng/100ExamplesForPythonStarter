#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 15, 2018, 2:05 AM
 * Software: PyCharm
 * Project Name: Tutorial
两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵：
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]
"""

import numpy, random

while True:
    N = int(input("Dimensions: "))
    X = numpy.random.randint(10, 100, size=[N, N])
    Y = numpy.random.randint(10, 100, size=[N, N])

    print("X + Y = \n")
    print("%s\n+%s\n=%s\n" % (X, Y, X + Y))

