#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 15, 2018, 1:50 AM
 * Software: PyCharm
 * Project Name: Tutorial
题目：模仿静态变量(static)另一案例。
程序分析：演示一个python作用域使用方法
"""

class Num:
    nNum = 1
    def inc(self):
        self.nNum += 1
        print('In Num, nNum = %d' % self.nNum)

nNum = 2
inst = Num()


for i in range(3):
    nNum += 1
    print('The num = %d' % nNum)

    inst.inc()
    print('\n')