#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 15, 2018, 7:37 PM
 * Software: PyCharm
 * Project Name: Tutorial
题目：回答结果（结构体变量传递）。
程序分析：无。
"""


class student:
    x, c = 0, 0


def f(stu):
    stu.x = 20
    stu.c = 'c'


a = student()
a.x = 3
a.c = 'a'

f(a)

print(a.x, a.c)
