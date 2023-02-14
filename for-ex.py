x = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
for i in x :
    print(i)

y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in y :
    print(i, end ='\t')


for g in range (0,9):
    print (g, end ='\t')
print()

n = int(input("請輸入要列印錢符號的數量: "))
for x in range(n): # 迴圈次數為 n
    print("$", end ="")
print()