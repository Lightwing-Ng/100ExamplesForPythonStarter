#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 15, 2018, 4:56 AM
 * Software: PyCharm
 * Project Name: Tutorial
题目：字符串排序。
程序分析：无。
"""

str1 = input('input string:\n')
str2 = input('input string:\n')
str3 = input('input string:\n')
print(str1, str2, str3)

if str1 > str2:
    str1, str2 = str2, str1
if str1 > str3:
    str1, str3 = str3, str1
if str2 > str3:
    str2, str3 = str3, str2

print('after being sorted.')
print(str1, str2, str3)
