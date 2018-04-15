#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 14, 2018, 10:43 PM
 * Software: PyCharm
 * Project Name: Tutorial
题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
程序分析：请抓住分子与分母的变化规律。
"""

a = 2.0
b = 1.0
l = []
l.append(a / b)

for i in range(1, 1000):
    b, a = a, a + b
    l.append(a / b)

print(l)