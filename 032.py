#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 15, 2018, 12:29 AM
 * Software: PyCharm
 * Project Name: Tutorial
题目：按逗号分隔列表。
程序分析：无
"""

L = []
for x in range(100):
    L.append(int((x + 50) * (x - 80)))
s1 = ', '.join(str(n) for n in L)

print(s1)
