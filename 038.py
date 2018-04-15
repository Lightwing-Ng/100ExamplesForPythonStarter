#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 15, 2018, 12:58 AM
 * Software: PyCharm
 * Project Name: Tutorial
题目：求一个3*3矩阵主对角线元素之和。
程序分析：利用双重for循环控制输入二维数组，再将a[i][i]累加后输出。
"""

import random, numpy

while True:
    N = int(input("The dimensions of the array: "))
    array = numpy.empty((N, N))
    for i in range(N):
        for j in range(N):
            array[i][j] = random.randint(1, 20)

    sum = 0
    for i in range(N):
        sum += int(array[i][i])

    print(array)
    print(sum)