#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 14, 2018, 11:12 PM
 * Software: PyCharm
 * Project Name: Tutorial
题目：利用递归方法求5!。
程序分析：递归公式：fn=fn_1*4!
"""


def fac(N):
    if N == 0 or N == 1:
        return 1
    else:
        return N * fac(N - 1)

print(fac(5))