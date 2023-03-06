'''import random as r # 以別名方式匯入 random 模組
for i in range(10): # 執行 10 次
    print(r.randrange(2,500,2)) # 從 2 - 500 間取 10 個偶數
    
import random as t # 以別名方式匯入 random 模組
for i in range(10): # 執行 10 次
    print(t.randrange(100)) # 從 0 - 100 取隨機整數 '''

'''Mark Six numbers'''
import random as z # 以別名方式匯入 random 模組
s = []
for i in range(7): # 執行 7 次
    st = (z.randrange(49)) # 從 0 - 49 取隨機整數 
    s.append(st)
    s.sort()
print((s)) 