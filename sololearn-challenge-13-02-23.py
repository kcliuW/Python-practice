# Question 1
''' 
Choose valid ways of inserting a
new value in a list named lista.
'''
'''
a) lista.append(10)

b) lista += [10]
'''

# Question 2
# What is the output of this code?
def foo():
    try:
        print(1)
    finally:
        print(2)
foo()

# Question 3
# How to take integer input from the user?
'''
Answer : n = int(input())
'''

# Question 4
# What is the output of this code?
x = 2
y = x
z = y
if z is x:
    print(x)
else:
    print(x + 2)

# Question 5
# What is the output of this code?
my_num = 1234
a = str(my_num//1000%10) # Note = 1234//1000 = 1, then 1 % 10 = 1.
b = str(my_num//100%10)  # Note = 1234//100 = 12, then 12 % 10 = 2.
c = str(my_num//10%10)   # Note = 1234//10 = 123, then 123 % 10 = 3.
d = str(my_num//1%10)    # Note = 1234//1 = 1234, then 1234 % 10 = 4.
print(d+c+b+a)