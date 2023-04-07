'''
Question 1
'''
# What is the output of this code?
def ZeroRecursive(a):
    if a == []:
        return
    a[0] = 0
    ZeroRecursive(a[1:])
a = [1, 2, 3, 4]
ZeroRecursive(a)
print(a)

'''
Question 2
'''
# What is the output of this code?
a = 2
b = 3
c = 4
print(a**b*a**c)

'''
Question 3
'''
# What is the output of this code?
a = {"A", "B", "C", "D"}
b = {"B", "D", "E"}
c = {"E", "B", "A"}
print(b^c)  # b^c is XOR, that not in b or c, which means both in b and c return false(0)
            # In this case, "B", "E" will be eliminate, remain "A", "D".
print((b^c)-a)

'''
Question 4
'''
# What is the output of this code?
def f(num):
    return (num**2)/3
print(f(3))

'''
Question 5
'''
# What of the following data types is not supported in python?
# 1) Slice
# 2) String
# 3) List
# 4) Numbers

# Answer: Slice