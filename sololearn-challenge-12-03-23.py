'''
Question 1
'''
# Fill in the blanks to define a
# function named "sum" that takes
# two arguments, x and y and returns
# their sum.

def sum(x,y):
    return x + y

print(sum(4,6))

'''
Question 2
'''
# What is the output of this code?
a,b,c = 1, -4, 0
a = -b*2
c = -a*3
a = -b*2
print(c)

'''
Question 3
'''
# Which of the followings is invalid?

# Answer : int('20.18')

'''
Question 4
'''

# How many times will this code output "x"?

def test():
    print("x")
    return test

test ()()()()

'''
Question 5
'''
# Which of these statements are invalid?

# Answer : 1) a = 1//0 (ZeroDivisionError: integer division or modulo by zero)
#          2) a = 1/0  (ZeroDivisionError: division by zero)