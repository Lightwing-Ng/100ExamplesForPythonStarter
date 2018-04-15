#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 14, 2018, 11:53 PM
 * Software: PyCharm
 * Project Name: Tutorial
题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
程序分析：用情况语句比较好，如果第一个字母一样，则判断用情况语句或if语句判断第二个字母。。
"""

WeekDays = {
    1: 'baby',
    2: 'back',
    3: 'background',
    4: 'backward',
    5: 'bacteria',
    6: 'bad',
    7: 'badminton',
    8: 'baggage',
    9: 'balance',
    11: 'haberdashery',
    12: 'habitable',
    13: 'habitual',
    14: 'hackney',
    15: 'haddock',
}

while True:
    count = 0
    tempResult = []

    while True:
        key = str(input("Please take a guess of the Weekdays: "))
        if count == 0:
            for x in WeekDays.items():
                if x[1][count] == key:
                    print(x[1])
                    tempResult.append(x[1])
        else:
            for x in tempResult:
                if x[count] != key:
                    tempResult.remove(x)
            for x in tempResult:
                print(x)
                if len(tempResult) == 1:
                    break
        count += 1
