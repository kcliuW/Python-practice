"""
讓使用者輸入密碼, 並且進行密碼驗證.
輸入次數以三次為限, 超過三次則不准登入.
預設密碼為3388.
"""

password = 3388
i = 1
while i <= 3:
    new_pw = (input("請輸入密碼: "))
    if (len(new_pw)!= 4):
        print("請輸入 4 位數字密碼!!")
    if int(new_pw)!= password:
        print("密碼發生錯誤!!, 請再次輸入!")
        i = i + 1
        continue
    else:
        print("密碼正確!!")
        break
if i > 3:
    print("密碼錯誤三次, 取消登入!!")