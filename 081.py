#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 15, 2018, 5:27 AM
 * Software: PyCharm
 * Project Name: Tutorial
题目：809*??=800*??+9*?? 其中??代表的两位数, 809*??为四位数，8*??的结果为两位数，9*??的结果为3位数。求??代表的两位数，及809*??后的结果。
程序分析：无。
"""

for x in range(10, 100):
    if 1000 <= x * 809 < 10000 and \
            10 <= 8 * x < 100 and \
            100 <= 9 * x < 1000:
        print(x)
