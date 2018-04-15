#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 15, 2018, 3:24 AM
 * Software: PyCharm
 * Project Name: Tutorial
题目：画椭圆。　
程序分析：使用 Tkinter。
"""

from tkinter import *

x, y = 360, 160
top, bottom = y - 30, y - 30
canvas = Canvas(width=400, height=600, bg='white')

for i in range(40):
    canvas.create_oval(250 - top, 250 - bottom, 250 + top, 250 + bottom)
    top -= 2
    bottom += 2
canvas.pack()

mainloop()
