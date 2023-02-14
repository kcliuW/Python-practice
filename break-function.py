num = int(input("資料處理到幾月? (1 ~ 12) "))

for i in range(12):
    print(i + 1, "月的資料.")
    if ( i + 1) == num:
        break