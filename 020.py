#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 14, 2018, 9:48 PM
 * Software: PyCharm
 * Project Name: Tutorial
"""

InitHigh = 100
count = 0
sum = InitHigh

while count < 10:
    count += 1
    sum += InitHigh
    InitHigh /= 2

print(sum)