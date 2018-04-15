#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 15, 2018, 1:39 AM
 * Software: PyCharm
 * Project Name: Tutorial
题目：模仿静态变量的用法。
程序分析：无。
"""


def varFunc():
    var = 0
    print("var = %d" % var)
    var += 1


if __name__ == '__main__':
    for i in range(3):
        varFunc()


# 类的属性
class Static:
    StaticVar = 5

    def varFunc(self):
        self.StaticVar += 1
        print(self.StaticVar)


print(Static.StaticVar)

a = Static()

for i in range(3):
    a.varFunc()
