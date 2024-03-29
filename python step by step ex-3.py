'''
Question 1
'''
#假設某道路全長 765 公尺, 現欲在橋的兩旁兩端每 17 公尺插上一支旗子
#(此範例假設頭尾都插旗子), 如果每支旗子需 210 元, 請設計一個程式
#計算共要花費多少元?

x = (765 / 17 + 1) * 2 * 210
print("共需花費: %d 元" %x)

'''
Question 2
'''
#請設計一程式, 輸入任何一個三位數以上的整數, 並未利用餘數運算子 (%)
#所寫成的運算式來輸出其百位數的數字. 例如 4976, 則輸出 9, 254637
#則輸出 6.

print("請輸入三位數以上整數: ", end="")
num = int(input())
num = (num /100) % 10
print("百位數的數字為: %d" %num)

'''
Question 3
'''
#請設計一程式,能夠讓使用者輸入準備兌換的金額, 並能輸出所能兌換的
#百元, 50 元紙鈔與 10 元硬幣的數量.
print("請輸入將兌換金額: ", end="")
num = int(input())
hundred = num//100
fifty = (num-hundred*100)//50
ten = (num-hundred*100-fifty*50)//10
print("百元鈔有 %d 張五十元鈔有 %d 張十元鈔有 %d 張" %(hundred,fifty,ten))