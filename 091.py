#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 15, 2018, 8:35 PM
 * Software: PyCharm
 * Project Name: Tutorial
题目：时间函数举例1。
程序分析：无。
"""

import time
print(time.ctime(time.time()))
print(time.asctime(time.localtime(time.time())))
print(time.asctime(time.gmtime(time.time())))