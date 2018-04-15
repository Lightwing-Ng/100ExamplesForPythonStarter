#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 14, 2018, 4:09 AM
 * Software: PyCharm
 * Project Name: Tutorial
题目：有四个数字：0-9，能组成多少个互不相同且无重复数字的三位数？各是多少？
程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。
"""
count = 0
for i in range(0, 10):
    for j in range(0, 10):
        for k in range(0, 10):
            if i != j and i != k and j != k:
                count += 1
                result = i * 100 + j * 10 + k
                print("No.%s: %s" % (count, result))
