'''Question 1'''
# What is the output of this code?
A = 12
B = 3
x = A%B
print(x)

'''Question 2'''
# What is the output of this code?
s = 'abc'
i = iter(s)
next(i)
print(next(i))

'''Question 3'''
# What is the output of this code?
a = 3
def sumofnum(*nums):
    return sum(nums)
print(sumofnum(a,a**a,a*4))

'''Question 4'''
# What is the output of this code?
o = "j"
e = "a"
o = o + e + "v" # o = "j"+"a"+"v"
o = o + e       # o = "j"+"a"+"v"+"a"
m = o           # m = o = "java"
print(m)

'''Question 5'''
# What is the output of this code?
X = (10**2-1)
print(X)