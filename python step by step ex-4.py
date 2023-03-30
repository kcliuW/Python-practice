'''
Question 3
'''
# 以下程式請改成表達運算式只要簡單一行程式就能達成同樣的目的.
x = int(input("Please input a number: "))
if x % 2 == 0:
    y = "偶數"
else:
    y = "奇數"
print('{0}'.format(y))

# Answer
a = int(input("Please input a number: "))
print('{0}'.format("偶數" if a % 2 == 0 else "奇數")) # 表達運算式

'''
Question 4
'''
# 請設計一程式讓使用者輸入一整數, 並判斷是否為 5 或 7 的倍數, 不過
# 卻不能為 35 的倍數.

num = int(input("請任意輸入一個整數: "))
if num % 5 == 0 or num % 7 == 0: # 判斷是否為 5 或 7 的倍數
    if num % 35 != 0:
        print("符合所要的條件.")
    else:
        print("不符合所要的條件.") # 為 35 的倍數
else:
   print("不符合所要的條件.") 
   
'''
Question 5
'''
# 請寫出下列程式的輸出結果.
number = 84
if number % 4 == 0:
    if number % 7 == 0:
        print("{} 是 4 與 7 的 公倍數".format(number))
else:
        print("{} 不是 4 的倍數".format(number))

'''
Question 6
'''
# 請問以下程式碼的執行結果?
cost = 180
if cost >= 125:
    print("Expensive")

'''
Question 7
'''
# 請問以下程式碼的執行結果?
X = 121
print("7的倍數" if x % 7 == 0 else "不是7的倍數")

'''
Question 8
'''
# 請問以下程式碼的執行結果?
height = 180
if height >= 175:
    print("Tall")
    
'''
Question 9
'''
# 請問以下程式碼的執行結果?
Z = 20
print("5的倍數" if x % 7 == 0 else "不是5的倍數")