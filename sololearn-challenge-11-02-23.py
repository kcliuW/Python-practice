# What is the output of this code?
# Question 1
nums = [10, 9, 8, 7, 6, 5]
nums[3] = nums[5] - 4
if 1 in nums:
    print("true")
else:
    print("false")

# Question 2
# What is the output of this code?
print('abcde'[::-1])

# Question 3
# What is the output of this code?
def func1():
    pass
def func2(n):
    if n%2 == 0:
        return None
print(func1() == func2(6))
print(func1() == func2(3))

# Question 4
# What is the output?
print(1+2*3-4**(4-2))

# Question 5
# What is the output of this code?
words = ["hi", "solo", "learn"]
more = [x*len(x) for x in words]
print(len(max(more, key=len)))