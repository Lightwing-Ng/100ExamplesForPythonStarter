#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 15, 2018, 5:32 AM
 * Software: PyCharm
 * Project Name: Tutorial
题目：八进制转换为十进制
程序分析：无。
"""

if __name__ == '__main__':
    n = 0
    p = input('input a octal number:\n')
    for i in range(len(p)):
        n = n * 8 + ord(p[i]) - ord('0')
    print(n)