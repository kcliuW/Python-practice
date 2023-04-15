'''
Question 1
'''
# What is the output of this code?

def bar():
    x = 1
    def foo():
        print('x' in globals(), 'x' in locals())
        foo()
        print(foo())
bar()
print(bar())

'''
Question 2
'''
# What is the output of this code?
x = (0,1,2)
[a,b,c] = x
print(a+b+c)

'''
Question 3
'''
# What is the output of this code?
class MyClass:
    def __init__(self,n):
        self.x = n
    def set_y(self):
        self.y = self.x * 2
obj = MyClass(2)
# print(obj.x + obj.y) 

# Answer : 
# Error . Reason  is "AttributeError": 'MyClass' object has no attribute 'y'

'''
Question 4
'''
# What is the output of this code?
from random import randint
a = [2,3,7,8]
i = randint(1,2)
print(a[i]%2)

'''
Question 5
'''
# Fill in the blank to output a random
# number between 2 and 5.

import random
print(random.randint(2,5))


