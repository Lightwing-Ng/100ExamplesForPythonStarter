#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 14, 2018, 4:52 AM
 * Software: PyCharm
 * Project Name: Tutorial
题目：输入三个整数x,y,z，请把这三个数由小到大输出。
程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。
"""

l = []
variable_name = ['x', 'y', 'z']
for i in variable_name:
    x = int(input("%s = " % i))
    l.append(x)
l.sort()

for x in l:
    print(x, end=' ')
