#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 15, 2018, 2:55 AM
 * Software: PyCharm
 * Project Name: Tutorial
题目：取一个整数a从右端开始的4〜7位。
程序分析：可以这样考虑：
(1)先使a右移4位。
(2)设置一个低4位全为1,其余全为0的数。可用~(~0<<4)
(3)将上面二者进行&运算。
"""

import random

a = random.randint(10, 100)
b = a >> 4
c = ~(~0 << 4)
d = b & c

print("%o\t%o" % (a, d))
