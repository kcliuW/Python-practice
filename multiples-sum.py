t = int(input("Please input the numbers: "))
i = sum(range(0, t, 3))
print(i)

j = sum(range(0, t, 5))
print(j)
    
k = sum(range(0, t, 15))

s = i + j - k

print(s)

s = int(input("Please enter the numbers of siblings: "))
c = int(input("Please enter the numbers of candies: "))
if c % s == 0:
    print("give away")
else:
    print("eat them yourself")
