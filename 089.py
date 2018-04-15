#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 15, 2018, 7:43 PM
 * Software: PyCharm
 * Project Name: Tutorial
题目：某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，加密规则如下：每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换。
程序分析：无。
"""

import random


def encryption(N):
    N = int(N)
    return (N + 5) % 10


while True:
    N = int(input("Press Number of Digits: "))
    A, B = 10, 1
    Rand = random.randint(A ** (N - 1), A ** N)
    print("Original Number: %s." % format(Rand, ','))

    # Digital decomposition
    res = []
    count = N
    while count > 0:
        res.append(int(Rand % A / B))
        A, B = 10 * A, A
        count -= 1

    # Encryption Number
    res_ecp = list(map(encryption, res))

    if N >= 2:
        # swap if the length of str is greater than 1
        for i in range(0, int(len(res_ecp) / 2 - 1)):
            res_ecp[i], res_ecp[len(res_ecp) - 1 - i] = res_ecp[len(res_ecp) - 1 - i], res_ecp[i]

    B, EncryptionNumber = 1, 0
    for x in res_ecp:
        EncryptionNumber += int(x) * B
        B *= 10

    print("Encryption Number: %s.\n" % format(EncryptionNumber, ','))
