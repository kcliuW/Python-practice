import random
result = random.randint(1,99)
counter = 0

print("猜猜今晚樂透號碼 (2位數): ", end="")
selection = int(input("請輸入號碼: ")) 
for counter in range(2):
    if selection != result:
        print("猜錯了....")
        counter += 1 
        selection = int(input("請再嘗試輸入號碼:"))
        if counter == 2:
            print("猜錯了....")
            print("答案是 %d" %result)
    else:    
        print("你猜中了!")