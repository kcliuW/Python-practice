a = 1
n = int(input("請輸入一個數字 :"))
print("%d 的所有因數為:" %n,end="")
while a <= n: # 定義 while 迴圈, 且設定條件為 a<=n
    if n%a == 0: # 當 n 能夠被 a 整除時 ~ 則 a 就是 n 的因數
        print("%d" %a,end="")
        if n!=a: print(",",end="")
    a += 1  # a 值遞增 1      