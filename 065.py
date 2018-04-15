#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 15, 2018, 3:33 AM
 * Software: PyCharm
 * Project Name: Tutorial
题目：一个最优美的图案。　　
程序分析：无。
"""

import math
from tkinter import *


class PTS:
    def __init__(self):
        self.x = 0
        self.y = 0


points = []


def LineToDemo():
    screenX, screenY = 400, 400
    canvas = Canvas(width=screenX, height=screenY, bg='white')

    AspectRatio = 0.85
    MAXPTS = 15
    h, w = screenX, screenY
    Xcenter = w / 2
    Ycenter = h / 2
    radius = (h - 30) / (AspectRatio * 2) - 20
    step = 360 / MAXPTS
    angle = 0.0

    for i in range(MAXPTS):
        rads = angle * math.pi / 180.0  # 弧度
        p = PTS()
        p.x = Xcenter + int(math.cos(rads) * radius)
        p.y = Ycenter - int(math.sin(rads) * radius * AspectRatio)
        angle += step
        points.append(p)

        canvas.create_oval(
            Xcenter - radius,
            Ycenter - radius,
            Xcenter + radius,
            Ycenter + radius
        )

    for i in range(MAXPTS):
        for j in range(i, MAXPTS):
            canvas.create_line(
                points[i].x,
                points[i].y,
                points[j].x,
                points[j].y
            )

    canvas.pack()
    mainloop()


if __name__ == '__main__':
    LineToDemo()
