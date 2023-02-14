for a in range(10): # 外層 for 迴圈控制 y 軸輸出
    for b in range(1,a+1): # 內層 for 迴圈控制 x 軸輸出
        if b == 6:
            continue
        print("%d" %b, end=" ") # 印出 b 的值
    print()