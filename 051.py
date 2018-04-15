#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 15, 2018, 2:46 AM
 * Software: PyCharm
 * Project Name: Tutorial
题目：学习使用按位与 & 。
程序分析：0&0=0; 0&1=0; 1&0=0; 1&1=1。
"""

a = 0o77
b = a & 3
print('a & b = %d' % b)

b &= 7
print('a & b = %d' % b)
