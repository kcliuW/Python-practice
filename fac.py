# 計算 10! 的值
product = 1
for i in range(1,11): # 定義 for 迴圈
    product*=i
print("product=%d" %product) # 印出乘積的結果

# 產生圖案
n = int(input(" 請輸入要產生圖案的魔術數字: "))
for x in range(1, n + 1): #迴圈次數為 n
    for j in range(1, x + 1):
        print("*", end="")
    print()