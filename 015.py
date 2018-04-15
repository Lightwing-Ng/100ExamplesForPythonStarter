#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 14, 2018, 8:36 PM
 * Software: PyCharm
 * Project Name: Tutorial
题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
程序分析：程序分析：(a>b)?a:b这是条件运算符的基本例子。
"""

while True:
    score = int(input("Please type your score(0-100): "))

    if score >= 95:
        grade = 'A+'
    elif score >= 90:
        grade = 'A'
    elif score > 60:
        grade = 'B'
    else:
        grade = 'F'

    print("Your Grade is: %s." % grade)
