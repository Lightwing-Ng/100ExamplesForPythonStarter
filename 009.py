#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 14, 2018, 7:47 PM
 * Software: PyCharm
 * Project Name: Tutorial
题目：暂停一秒输出。
程序分析：使用 time 模块的 sleep() 函数
"""

import time

number = []
alpha = []
for i in range(33, 1000):
    number.append(i)
    alpha.append(chr(i))
ASCii = dict(zip(number, alpha))

for k, v in dict.items(ASCii):
    print("%s - %s" % (k, v))
    # time.sleep(0.1)
