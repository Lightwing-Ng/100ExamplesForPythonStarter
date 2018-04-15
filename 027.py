#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 14, 2018, 11:14 PM
 * Software: PyCharm
 * Project Name: Tutorial
题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
程序分析：无。
"""

# res = []
# total = 5
# count = total
# while count:
#     print("Please type a String(%d/%d): " % (total - count + 1, total))
#     x = input()
#     res.append(x)
#     count -= 1


def output(s, l):
    if l == 0:
        return
    print(s[l - 1])
    output(s, l - 1)


s = input('Input a string: ')
l = len(s)
output(s, l)

