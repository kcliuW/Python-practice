print("停車超過 1 小時, 每小時收費 40 元.")
t = int(input("請輸入停車時間: "))
if t >= 1:
    total = t * 40
    print("停車超過 %d 小時, 總費用為: %d 元" %(t, total))