# -*- coding: utf-8 -*-
"""
程式名稱 : 閏年判斷程式
題目要求 :
輸入西元年 ( 4 位數的整數 year) 判斷是否閏年
條件 1. 逢 4 閏 (除 4 可整除) 而且逢 100 不閏 (除 100 不可整除)
條件 2. 逢 400 閏 (除 400 可整除)
滿足兩個條件之一即是閏年
"""
year = int(input("請輸入西元年份:"))
if (year % 4 == 0 and year % 100 !=0) or (year % 400 == 0):
    print("{0}是閏年".format(year))
else:
    print("{0}是平年".format(year))