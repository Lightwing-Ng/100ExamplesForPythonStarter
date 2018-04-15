#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 14, 2018, 8:47 PM
 * Software: PyCharm
 * Project Name: Tutorial
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
程序分析：利用 while 或 for 语句,条件为输入的字符不为 '\n'。
"""

import string

s = """
Mr Trump’s desire to make good on his promise to punish the “crimes of a monster” appear to have stalled his plans to pull America out of Syria. About 2,000 American troops are based in the north-east of the country, where they fight alongside a Kurdish-led force against what is left of the Islamic State jihadist group. “We look forward to the day when we can bring our warriors home,” said Mr Trump, while announcing the attack. But his advisers want America to stay in Syria. For this administration, punishing Mr Assad is likely to prove easier than devising a coherent Syria policy.
"""

letters = 0
space = 0
digit = 0
others = 0
count = 0

while count < len(s):
    c = s[count]
    count += 1
    if c.isalpha():
        letters += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        digit += 1
    else:
        others += 1

print(
    (
            """
TotalLen: %3d,
Letters : %3d,
Spaces  : %3d,
Digits  : %3d,
Others  : %3d.
""" % (len(s), letters, space, digit, others)
    ).center(50, ' ')
)
