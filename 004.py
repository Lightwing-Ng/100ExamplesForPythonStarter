#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 14, 2018, 4:41 AM
 * Software: PyCharm
 * Project Name: Tutorial
题目：输入某年某月某日，判断这一天是这一年的第几天？
程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天：
"""

months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)


def isLeapYear(n):
    if (n % 400 == 0) or ((n % 4 == 0) and (n % 100 != 0)):
        return True
    return False


while True:
    year = int(input('Year: '))
    month = int(input('Month: '))
    day = int(input('Day: '))

    sum = 0
    if 0 < month <= 12:
        sum = months[month - 1]
    sum += day

    if isLeapYear(year) and month > 2:
        sum += 1

    print("It's the %dth day of %s." % (sum, year))
