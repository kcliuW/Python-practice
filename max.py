Max = 0
num = int(input("準備輸入數字的個數:"))
for i in range(num):
    print(">",end="")
    temp = int(input())
    if Max < temp:
        Max = temp
print(" 這些數字中的最大值為: %d" % Max)