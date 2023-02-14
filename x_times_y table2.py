a = int(input("請輸入數字: "))
b = int(input("請輸入數字: "))

print(f"{a}乘{b}乘法表".center(74))

for i in range(a,(b+1)):
    for j in range(a,(b+1)):
        print(f'{i}x{j}={i * j:2} ', end='')
    print()
