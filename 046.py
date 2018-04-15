#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 15, 2018, 2:15 AM
 * Software: PyCharm
 * Project Name: Tutorial
题目：求输入数字的平方，如果平方运算后小于 50 则退出。
程序分析：无
"""

TRUE = 1
FALSE = 0


def SQ(x):
    return x * x


while True:
    print('如果输入的数字小于 50，程序将停止运行。')
    again = 1
    while again:
        num = int(input('请输入一个数字：'))
        print('运算结果为: %s' % format(SQ(num), ','))
        if SQ(num) >= 50:
            again = TRUE
        else:
            again = FALSE
