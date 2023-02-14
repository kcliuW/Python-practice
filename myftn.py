def myftn(*nums):
    t=1
    for num in nums:
        t*=num
    return t

print(myftn(1,3,4,5))