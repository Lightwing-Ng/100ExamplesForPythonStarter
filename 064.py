#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 15, 2018, 3:31 AM
 * Software: PyCharm
 * Project Name: Tutorial
题目：利用ellipse 和 rectangle 画图。。　
程序分析：无。
"""

from tkinter import *

canvas = Canvas(width=400, height=600, bg='white')
left, right, top, num = 20, 50, 50, 15

for i in range(num):
    canvas.create_oval(250 - right, 250 - left, 250 + right, 250 + left)
    canvas.create_oval(250 - 20, 250 - top, 250 + 20, 250 + top)
    canvas.create_rectangle(20 - 2 * i, 20 - 2 * i, 10 * (i + 2), 10 * (i + 2))
    right += 5
    left += 5
    top += 10
canvas.pack()

mainloop()
