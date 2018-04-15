#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 14, 2018, 9:33 PM
 * Software: PyCharm
 * Project Name: Tutorial
"""


def factorization(n):
    res = []
    for x in range(1, int(n / 2 + 1)):
        if n % x == 0:
            res.append(x)
    return res


def isCompleteNum(n):
    res = factorization(n)
    sum = 0
    for x in res:
        sum += x
    if sum == n:
        return True
    return False


for i in range(2, 10000):
    if isCompleteNum(i):
        print(i, end=' = ')
        factors = factorization(i)

        count = 0
        for x in factors:
            count += 1
            if count != len(factors):
                print(x, end=' + ')
            else:
                print(x, end='.\n')
