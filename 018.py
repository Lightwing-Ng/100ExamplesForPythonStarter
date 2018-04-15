#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 14, 2018, 9:04 PM
 * Software: PyCharm
 * Project Name: Tutorial
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
程序分析：关键是计算出每一项的值。
"""


def GenNum(base, times):
    sum = 0
    while times > 0:
        times -= 1
        sum += base * 10 ** times
    return sum


while True:
    n = int(input("n = "))
    base = int(input("base = "))

    res = []
    sum = 0
    for i in range(1, n + 1):
        res.append(GenNum(base, i))

    count = 0
    for x in res:
        count += 1
        sum += int(x)
        if count != n:
            print(('%s' % x), end=' + ')
        else:
            print(('%s' % x), end=' = ')
    print(format(sum, ','), end='.\n')
