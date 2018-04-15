#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 15, 2018, 8:37 PM
 * Software: PyCharm
 * Project Name: Tutorial
题目：时间函数举例2。
程序分析：无。
"""

import time
start = time.time()

for i in range(3000):
    print(format(i, ','))

end = time.time()

print(end - start)