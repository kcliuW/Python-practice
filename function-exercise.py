'''MC Question 1'''
# What is the key word of Python function?
# Answer is "def"

'''MC Question 2'''
# Which operators can perform Function call?
# Answer is "()"

'''MC Question 3'''
s = int(9.7)
print(s)

'''MC Question 4'''
m = divmod(62,7)
print(m)

'''MC Question 5'''
list_1 = [8, 23, 54]
print(max(list_1))

'''Practice Question'''

# 1. 如果要自訂一個可以傳3個參數的函數，回傳值為這3個參數的總和，該如何做？
# 解答：
def funcx(a,b,c):
    x = a + b +c
    return x
   
print(funcx(1,2,3))

#2. 請問以下程式的執行結果？
def func(a,b):
    x = a * b+6
    print(x)

print(func(3,2))

#3. 請問以下程式的執行結果？
def funct(a,b):
    p1 = a + b
    p2 = a % b
    return p1, p2
 
num1 ,num2 = funct(22, 3)
print(num1,num2)    

#4. 請問以下程式的執行結果？
def factorial(*arg):
    product=1
    for n in arg:
        product *= n
    return product

ans3=factorial(3,3,3)
print(ans3)

#5.請問以下程式的執行結果？
def Pow(x,y):
    p=1
    for i in range(y):
        p *= x
    return p

x,y=2,6
print(Pow(x,y))

#6. 請問以下程式的執行結果？
def funcc(x,y,z):
    formula = x+y+z
    return formula

print(funcc(z=5,y=2,x=7))
print(funcc(x=7, y=2 , z=5))

#7. 請問以下程式的執行結果？
result = lambda x : 3*x*x-1  
print(result(2))

'''8. 試比較自訂函數與lambda()函數的異同。
解答：
◆ 自訂函數的函數名稱，可作為呼叫lambda()函數的變數名稱。
◆ 定義函數時，函數主體有多行指令；但是lambda()函數只能有一行運算式。
◆ 自訂函數有名稱，但lambda()函數無名稱，lambda()函數必須指定一個變數來儲存運算結果。
◆ 自訂函數以return指令回傳；lambda()函數由變數指定變數儲存。
◆ lambda()函數必須以變數名稱（例如上例中的formula變數）來呼叫lambda()函數，依其定義傳入參數。
'''


