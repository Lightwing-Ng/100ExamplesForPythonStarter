#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 15, 2018, 3:11 AM
 * Software: PyCharm
 * Project Name: Tutorial
题目：画图，学用rectangle画方形。　　　
程序分析：
    rectangle(int left, int top, int right, int bottom)
"""
if __name__ == '__main__':
    from tkinter import *

    root = Tk()
    root.title('Canvas')
    canvas = Canvas(root, width=400, height=400, bg='yellow')
    x0, y0, y1, x1 = 263, 263, 275, 275

    for i in range(20):
        canvas.create_rectangle(x0, y0, x1, y1)
        x0 -= .5 * i
        y0 -= .5 * i
        x1 += .5 * i
        y1 += .5 * i

    canvas.pack()
    root.mainloop()
