'''Question 1'''
'''
Fill in the blanks to create a
function that calculates a sum of
all digits in the given number.
For example, "123" will result into 6.
'''

import math
def digitSum(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n = math.floor(n / 10)
    return sum

print(digitSum(123))

'''Question 2'''
# What is the output of the following code?
x, y = 4, 6
a = "{x}".format(x = y), + 2, "{y}".format(y = 10)
print(a)

'''Question 3'''
# We can not have a list inside a list. Answer: False

'''Question 4'''
# Which of the following is type of a number? Answer: 1) integers , 2) float.

'''Question 5'''
# What is the output of this code?
x = len(3*['apple']*3)
y =(3*['apple']*3)
print(x)
print(y)