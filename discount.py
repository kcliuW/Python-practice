cost = float(input("請輸入消費總金額:"))
if cost >= 100000:
    n = 85
    cost = cost * (n/100) # 10萬元以上打 85 折
elif cost >= 50000:
    n = 9
    cost = cost * (n*10/100) # 5 萬元到 10 萬元之間打 9 折
else:
    n = 95
    cost = cost * (n/100)# 5 萬元以下打 95 折
print("實際消費總額: %.1f 元," %cost, "折扣: %d 折" %n) 