#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 15, 2018, 2:19 AM
 * Software: PyCharm
 * Project Name: Tutorial
题目：数字比较。
程序分析：无
"""

import random

if __name__ == '__main__':
    i = random.randint(10, 100)
    j = random.randint(10, 100)
    if i > j:
        print('%d 大于 %d' % (i, j))
    elif i == j:
        print('%d 等于 %d' % (i, j))
    elif i < j:
        print('%d 小于 %d' % (i, j))
    else:
        print('未知')
