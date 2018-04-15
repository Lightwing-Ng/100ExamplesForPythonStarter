#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 15, 2018, 8:57 PM
 * Software: PyCharm
 * Project Name: Tutorial
题目：从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为止。
程序分析：无。
"""

from sys import stdout
import os, sys

filename = str(input("Please type the Filename: "))
fp = open(filename, 'w')
ch = input("Please Start to write here, ends with #:\n")

while ch != '#':
    fp.write(ch)
    stdout.write(ch)
    ch = input('')

fp.close()


