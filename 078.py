#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 15, 2018, 4:55 AM
 * Software: PyCharm
 * Project Name: Tutorial
题目：找到年龄最大的人，并输出。请找出程序中有什么问题。
程序分析：无。
"""

person = {
    "li": 18, "wang": 50, "zhang": 20, "sun": 22}
m = 'li'
for key in person.keys():
    if person[m] < person[key]:
        m = key

print('%s,%d' % (m, person[m]))
