i = int(input("請輸入開始數字: "))
j = int(input("請輸入完結數字: "))

if j % 2 == 0:
    print(f"顯示{i}到{j-2}之間的偶數: ")
else:
    print(f"顯示{i}到{j}之間的偶數: ")

for a in range(i,j,2):
    print(a)
        
        