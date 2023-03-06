import random as r # 為 random 模組取別名
for j in range(6): # 以迴圈執行 6 次
    print(r.randint(1,42), end = ' ') # 產生 1 - 42 的整數亂數
print() # 換行 1
for j in range(3): # 以迴圈執行 3 次
    print(r.uniform(1,10), end = ' ') # 產生 1 - 10 間的亂數