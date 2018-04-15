#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 15, 2018, 1:46 AM
 * Software: PyCharm
 * Project Name: Tutorial
题目：学习使用auto定义变量的用法。
程序分析：没有auto关键字，使用变量作用域来举例吧。
"""

num = 2

def autoFunc():
    num = 1
    print("internal block num = %d" % num)
    num += 1

for i in range(3):
    print('The num = %d' % num)
    num += 1
    autoFunc()