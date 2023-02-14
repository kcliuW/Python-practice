print(" 目前提供的選擇如下:")
print(" 0. 查詢其他相關的點心資料")
print(" 1. 吉列漢堡")
print(" 2. 咖哩珍豬飽")
print(" 3. 六件麥樂雞")
print(" 請點選您需要的項目:")

Select = int(input()) # 輸入餐點項目
if Select == 0: # 選擇第 0 項
    print(" 請稍等... 正在查詢其他相關的點心資料")
elif Select == 1: # 選擇第 1 項
    print("這個項目的單價 :%d" %45)
elif Select == 2: # 選擇第 2 項
    print("這個項目的單價 :%d" %55)
elif Select == 3: # 選擇第 3 項
    print("這個項目的單價 :%d" %65)
else: # 輸入錯誤的處理
    print("您可能輸入錯誤.... 請重新輸入")
    