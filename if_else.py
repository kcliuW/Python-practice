num = int(input('請輸入一個整數: '))
if num%5:
    print(num, '不是 5 的倍數')
else:
    print(num, '為 5 的倍數')

value = int(input('請任意輸入一個整數: ')) # 輸入一個整數
# 判斷是否為 2 或 3 的倍數
if value % 2 == 0 or value % 3 == 0:
    if value % 6 != 0:
        print("符合所要的條件")
    else:
        print("不符合所要的條件") # 為 6 的 倍數

else:
    print("不符合所要的條件")
