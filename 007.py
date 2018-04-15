#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 14, 2018, 6:57 PM
 * Software: PyCharm
 * Project Name: Tutorial
题目：将一个列表的数据复制到另一个列表中。
程序分析：使用列表[:]。
"""

l = []
for i in range(100):
    l.append(i ** 2)

b = l[:]

for x in b:
    print(format(x, ','))
