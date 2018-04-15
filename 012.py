#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 14, 2018, 8:12 PM
 * Software: PyCharm
 * Project Name: Tutorial
题目：判断101-200之间有多少个素数，并输出所有素数。
程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。
"""


def isPrime(n):
    for i in range(2, int(n ** 0.5)):
        if n % i == 0:
            return False
    return True


count = 0
for i in range(101, 100000):
    if isPrime(i):
        count += 1
        print(format(i, ','))
