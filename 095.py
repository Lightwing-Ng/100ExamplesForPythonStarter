#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 15, 2018, 8:53 PM
 * Software: PyCharm
 * Project Name: Tutorial
题目：字符串日期转换为易读的日期格式。
程序分析：无。
"""

from dateutil import parser
dt = parser.parse("Aug 28 2015 12:00AM")

print(dt)