#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 15, 2018, 4:44 AM
 * Software: PyCharm
 * Project Name: Tutorial
题目：放松一下，算一道简单的题目。
程序分析：无。
"""

if __name__ == '__main__':
    for i in range(5):
        n = 0
        if i != 1:
            n += 1
        if i == 3:
            n += 1
        if i == 4:
            n += 1
        if i != 4:
            n += 1
        if n == 3:
            print(64 + i)