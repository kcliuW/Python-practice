'''Question 1'''
# Fill in the blanks to print the
# numbers from 1 to 5
for i in range(5):
    print(i+1)
    
'''Question 2'''
# What is the output of this code?
a = [-2,3,"*",4,"+",5]
sum = 0
for i in a:
    if type(i) == int:
        sum = sum + i
print(sum)

'''Question 3'''
# What is the output of this code?
def fact(x):
    if x == 1:
        return 2
    else:
        return x + fact(x-1)
print(fact(3))

'''Question 4'''
# What is the output of this code?
a = {3,2,1}
b = [1,2,3]
print(list(a) == b)

'''Question 5'''
# It is a coding convention