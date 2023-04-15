k = int(input("請輸入 k 值 :"))
sigma = 0
for n in range(int(k) + 1):
    if (n % 2!=0):
        sigma += float(-1/(2*n+1))
    else:
        sigma += float(1/(2*n+1))
print("PI = %f" %(sigma*4))