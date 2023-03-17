num = 123
print(123)
num1 = bin(num) # 2 進位
print(num1)
num2 = oct(num) # 8 進位
print(num2)
num3 = hex(num) # 16 進位
print(num3)
print(int(num1,2)) # 將 2 進位的字串轉換成 10 進位數值
print(int(num2,8)) # 將 8 進位的字串轉換成 10 進位數值
print(int(num3,16)) # 將 16 進位的字串轉換成 10 進位數值

'''
int()
'''
num1 = 8
num2 = 12 + int(num1)
print(num2) # Result : 20


'''
float()
'''
num3 = 9.25
num4 = 6 + float(num3)
print(num4) # Result : 15.25

'''
str()
'''
num5 = 3.78
num6 = 5 + float(num5)
print("輸出的數值是 " + str(num6)) # Result : 8.78