import random as r # 以別名方式匯入 random 模組
for i in range(10): # 執行 10 次
    print(r.randrange(2,500,2)) # 從 2 - 500 之間取出 10 個偶數
    