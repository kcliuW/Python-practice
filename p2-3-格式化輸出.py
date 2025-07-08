score = 88
print("<基本輸出>")
print('\n'"開始輸出")
print(1,2,3)
print(4,5,6, sep="@")
print(7,8,9, sep="|", end=" ")
print(10,11,12, sep="*")
print("結束輸出") 

print('\n'"<[%] 格式化輸出>")
# 使用 % 格式化
print('\n'"大明的數學成績: %d" % score)
print("大明的數學成績: {}".format(score))
print(f"大明的數學成績: {score}") # f-string 格式化
print("大明的數學成績: {:d}".format(score))


print("%5s 的數學成績 : %5.2f" % ("小明", 95))  # % 格式化
print("%5s 的數學成績 : %5.2f" % ("志明", 80.2))

print('\n'"<整數輸出不同進制>")
numA = 100
print('\n'" 數字 %s 的浮點數 : %5.1f" % (numA, numA))  # % 格式化
print(" 數字 %s 的八進位 : %o" % (numA, numA))
print(" 數字 %s 的十六進位 : %x" % (numA, numA))
print(" 數字 %s 的二進位 : %s" % (numA, bin(numA)))