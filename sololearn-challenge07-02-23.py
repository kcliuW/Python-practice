# Question 1
# What is the output of this code?
nums = [3, 5, 15]
nums.append(30)
print(len(nums*5))


# Question 2
# What is the output of the following code?
'''
t = (1,2,[3,4])
t[2,0] = 5 # tuple is immutable, therefore the output is error
print(t)
'''


# Question 3
# What is the output of this code?
import re
str = 'Sololearn123'
print(re.sub(r'[aA-zZ]',"",str))


# Question 4
"Is the type of 'myboy' bool, given the code below?"
myboy = True #  Answer is "Yes"


# Question 5
# How many numbers does the list contain after this code ?
a = []
for i in range(1,10):
    if (i % 2 == 0) or (i % 3 == 0):
        a.append(i)
        print(a)

