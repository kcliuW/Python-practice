# In this example, we will see How to Limit Floats to Two Decimal Points in Python. 
# In python float precision to 2 floats in python, and python float precision to 3. 
# There are many ways to set the precision of the floating-point values. 
# Some of them are discussed below.

'''1. Using “%”:'''# “%” operator is used to format as well as set precision in python. 
                   #  This is similar to “printf” statement in C programming.
                   
'''2. Using format():'''# This is yet another way to format the string for setting precision.
 
'''3. Using round(x,n):'''# This function takes 2 arguments, number, and the number till 
                          # which we want decimal part rounded.
                          
# Python code to demonstrate precision
# and round()

# initializing value
a = 3.4536

# using "%" to print value till 2 decimal places
print("The value of number till 2 decimal place(using %) is : ", end="")
print('%.2f' % a)

# using format() to print value till 3 decimal places
print("The value of number till 3 decimal place(using format()) is : ", end="")
print("{0:.3f}".format(a))

# using round() to print value till 2 decimal places
print("The value of number till 2 decimal place(using round()) is : ", end="")
print(round(a, 2))

'''
Output : 
'''
# The value of number till 2 decimal place(using %) is : '3.45'
# The value of number till 3 decimal place(using format()) is : '3.453'
# The value of number till 2 decimal place(using round()) is : '3.45'