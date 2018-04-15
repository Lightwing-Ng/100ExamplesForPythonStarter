#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 15, 2018, 2:58 AM
 * Software: PyCharm
 * Project Name: Tutorial
题目：学习使用按位取反~。
程序分析：~0=1; ~1=0;
(1)先使a右移4位。
(2)设置一个低4位全为1,其余全为0的数。可用~(~0<<4)
(3)将上面二者进行&运算。
"""

a = 234
b = ~a
print('The a\'s 1 complement is %d' % b)
a = ~a
print('The a\'s 2 complement is %d' % a)
