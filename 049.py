#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 15, 2018, 2:21 AM
 * Software: PyCharm
 * Project Name: Tutorial
题目：使用lambda来创建匿名函数。
程序分析：无
"""

import random

MaxNum = lambda x, y: (x > y) * x + (x < y) * y
MinNum = lambda x, y: (x < y) * x + (x > y) * y

while True:
    a, b = random.randint(10, 100), random.randint(10, 100)
    print("Max of %s and %s is %s" % (a, b, MaxNum(a, b)))
    print("Min of %s and %s is %s" % (a, b, MinNum(a, b)))
    break
