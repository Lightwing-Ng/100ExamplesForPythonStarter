#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 15, 2018, 12:41 AM
 * Software: PyCharm
 * Project Name: Tutorial
题目：求100之内的素数。
程序分析：无。
"""

while True:
    lower = int(input("Lower Value: "))
    upper = int(input("Upper Value: "))

    for x in range(lower, upper + 1):
        # 素数大于 1
        if x > 1:
            for i in range(2, int(x ** 0.5)):
                if (x % i) == 0:
                    break
            else:
                print(format(x, ','))
