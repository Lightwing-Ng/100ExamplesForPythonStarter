#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 14, 2018, 11:48 PM
 * Software: PyCharm
 * Project Name: Tutorial
题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
程序分析：无。
"""

while True:
    N = input("Please input a number: ")
    str_N = str(N)

    isBackText = True
    for i in range(int(len(str_N) / 2)):
        if str_N[i] != str_N[-i - 1]:
            isBackText = False
            break

    if isBackText:
        print("It's a palindromes!")
    else:
        print("It's not a palindromes.")