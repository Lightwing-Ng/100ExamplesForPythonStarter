#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 14, 2018, 7:56 PM
 * Software: PyCharm
 * Project Name: Tutorial
题目：暂停一秒输出，并格式化当前时间。
程序分析：无
"""

import time

while True:
    print(time.strftime('%Y/%m/%d, %H:%M:%S', time.localtime(time.time())))
    time.sleep(1)
