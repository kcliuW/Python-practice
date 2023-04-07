'''
Question 1
'''
# Function can receive an array as a 
# parameter.

# Answer : True

'''
Question 2
'''
# What is the output of this code?
empty = [1]
def myfunc(x):
    return not x
print(myfunc(empty))

'''
Question 3
'''
# What is the output of this code?
import numpy as np
a = np.array([[0, 1, 2],[3, 4, 5]])
b = a.ravel()
print(b)       # Note : print(b) = [0 1 2 3 4 5]
# print(b[0,0])

# Answer : Error
# Reason : IndexError: too many indices for array: array is 1-dimensional, but 2 were indexed

'''
Question 4
'''
# What is the output of this code?
print(int("22") + int("22"))

'''
Question 5
'''
# What is the output of this code？
my_array = [0, 5, 6, 2, 4]
a = my_array[1]
b = my_array[4]
c = a*b/my_array[3]
print(c)