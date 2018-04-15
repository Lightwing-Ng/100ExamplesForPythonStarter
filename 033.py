#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 15, 2018, 12:37 AM
 * Software: PyCharm
 * Project Name: Tutorial
题目：练习函数调用。
程序分析：无。
"""


def hello_world():
    print('hello world')


def three_hellos():
    for i in range(3):
        hello_world()


if __name__ == '__main__':
    three_hellos()
