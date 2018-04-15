#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 15, 2018, 2:59 AM
 * Software: PyCharm
 * Project Name: Tutorial
题目：画图，学用circle画圆形。　　　
程序分析：无。
"""

from tkinter import *
import time

canvas = Canvas(width=800, height=600, bg='blue')
canvas.pack(expand=YES, fill=BOTH)

k = 1
j = 1
for i in range(0, 26):
    canvas.create_oval(310 - k,250 - k,310 + k,250 + k, width=1)
    k += j
    j += 0.4
    # time.sleep(1)


mainloop()