#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 15, 2018, 9:04 PM
 * Software: PyCharm
 * Project Name: Tutorial
题目：从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件"test"中保存。
程序分析：无。
"""

fp = open('test.txt', 'w')
string = input('please input a string:\n')
string = string.upper()
fp.write(string)
fp = open('test.txt', 'r')
print(fp.read())
fp.close()
