n = int(input("Please input a number: "))
print("Reverse output of number :", end="")
while n!=0:
    print("%d" %(n%10), end="") # get a residual number
    n//=10
print()