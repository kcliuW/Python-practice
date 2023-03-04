'''Question 1'''
# Fill in the blanks to print the answer
#"to get to the other side!" to the 
# printed question

a = "to get to the other side!"
b = "to get away from KFC!"
joke = [a,b]
print("Why did the chicken cross the road?")
print(joke[0])

'''Question 2'''
# Fill in the blanks to create a
# function that calculates a sum of
# all digits in the given number.
# For example, "123" will result into 6.

import math
def digitSum(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n = math.floor(n/10)
    return sum

print(digitSum(123))

'''Question 3'''
# What is the output of this code?
x = [1, 3, 5]
print(x in x)

'''Question 4'''
# What is the output of this code?
def do_twice(x):
    return x*2
numbers = [11,12,13,14]
res = list(map(do_twice, numbers))
print(res[1])

'''Question 5'''
# What is the output of this code?
my_dict = {0:'a', 1:'b', 2:'c', 3:'d'}
print(my_dict[3])