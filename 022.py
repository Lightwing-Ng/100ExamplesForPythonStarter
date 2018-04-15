#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 14, 2018, 9:57 PM
 * Software: PyCharm
 * Project Name: Tutorial
"""

import itertools

TeamA = ['A', 'B', 'C']
TeamB = ['Z', 'Y', 'Z']

InitRes = []
for i in TeamA:
    for j in TeamB:
        InitRes.append((i, j))

for x in InitRes:
    if x[0] == 'a' and x[1] == 'x':
        InitRes.remove(x)
    elif x[0] == 'c' and (x[1] == 'y' or x[1] == 'z'):
        InitRes.remove(x)
print("All Possible Rivals".center(20, ' '))
for x in InitRes:
    print(("%s vs %s" % (x[0], x[1])).center(20, ' '))
