#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 15, 2018, 8:40 PM
 * Software: PyCharm
 * Project Name: Tutorial
题目：时间函数举例3。
程序分析：无。
"""

import time

res = []
start = time.clock()
for i in range(1000000):
    # print(format(i, ',')) 5.201s
    # print(i) 4.699s
    res.append(i)  # 0.124s
end = time.clock()
print('different is %6.3f' % (end - start))
