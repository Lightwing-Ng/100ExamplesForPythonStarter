#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 14, 2018, 7:00 PM
 * Software: PyCharm
 * Project Name: Tutorial
题目：输出 9*9 乘法口诀表。
程序分析：分行与列考虑，共9行9列，i控制行，j控制列。
"""

for x in range(1, 10):
    print()
    for y in range(1, x + 1):
        print("%d×%d=%2d" % (x, y, x * y), end=' ')
