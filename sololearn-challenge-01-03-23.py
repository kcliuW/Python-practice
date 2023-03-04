'''Question 1'''
# What is the output of this code?
n = 123
result = 0
while(n > 0):
    remainder = int(n % 10)
    result = result * 10 + remainder
    n = int(n / 10)
print(result)

'''Question 2'''
# Fill in the blanks to output 4.0.
import math
a,b,c = 1,7,9
c,b = b,c
print(math.sqrt(c + b))

'''Question 3'''
# What is the output of this code?
print('The sum of {0} and {1} is {2}'.format(2, 10, 12))

'''Question 4'''
# What is the output of this code?
if 1 | 0:
    print('a')
else:
    print('b')

'''Question 5'''
# What is the output of this code?
letter = ['a','a','a']
print(letter.index('a'))