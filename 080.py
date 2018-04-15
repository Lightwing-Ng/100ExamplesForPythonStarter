#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 15, 2018, 4:58 AM
 * Software: PyCharm
 * Project Name: Tutorial
题目：海滩上有一堆桃子，五只猴子来分。第一只猴子把这堆桃子平均分为五份，多了一个，这只猴子把多的一个扔入海中，拿走了一份。第二只猴子把剩下的桃子又平均分成五份，又多了一个，它同样把多的一个扔入海中，拿走了一份，第三、第四、第五只猴子都是这样做的，问海滩上原来最少有多少个桃子？
程序分析：无。
"""


# def DividePeaches(N):
#     for x in range(5):
#         if N > 6 and (N - 1) % 5 == 0:
#             N = int((N - 1) / 5)
#         else:
#             return False
#
#     if N > 0:
#         return True
#
# for x in range(6, 10000):
#     if DividePeaches(x):
#         print(format(x, ','))

for a in range(1, 10000):
    for x in range(5):
        a = a * 5 + 1
    print(format(a, ','))
