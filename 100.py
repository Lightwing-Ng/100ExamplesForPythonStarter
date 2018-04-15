#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 15, 2018, 9:08 PM
 * Software: PyCharm
 * Project Name: Tutorial
题目：列表转换为字典。
程序分析：无。
"""
l1, l2 = [], []
for i in range(35, 200):
    l1.append(i)
    l2.append(chr(i))

d = dict(zip(l1, l2))

for k, v in d.items():
    print("%s: %s." % (k, v))
