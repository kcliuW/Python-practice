'''
Question 1
'''
# Choose the correct way to load a module:

# Answer : import math

'''
Question 2
'''
# Fill in the blanks to create a function
# that calculates a sum of all digits 
# in the given number. For examples,
# "123" will result into '6'.

import math
def digitSum(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n = math.floor(n / 10)
    return sum

print(digitSum(123))

'''
Question 3
'''
# What is the most probable output
# of this code?
import random
a = [1,2,3,4,5]
sum = 0
for i in range(1000):
    b = random.choice(a)
    sum += b
print(round(sum / 1000))

# The result of running this code will be a 
# single integer representing the average of the 
# 1000 random numbers generated from the list a.

# On average, the result should be close to the
# expected value of the average of the numbers in the a list, which is 3.

'''
Question 4
'''
# What is the output of this code?
a = 9
b = 27
c = 47
if a < b or b > c:
    print(b)
print(a)

'''
Question 5
'''
# What is the value of S?
A = set([1,3,6,78,35,55])
B = set([12,24,35,24,88,120,155])
S = list(A & B)
print(S)
