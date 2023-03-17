'''
Question 1
'''
# What is the output of this code?
list1 = [1,2,3,4]
list2 = [5,6,7,7]
print(len(list1 + list2))

'''
Question 2
'''
# What is the output of this code?
nums = [3,5,15]
nums.append(30)
print(len(nums*5))

'''
Question 3
'''
variable = 9

def function(variable):
    variable += 1
    print(variable)
    
function(7)

print(variable)

'''
Question 4
'''
# If you rename functions of an
# imported module using the as
# keyword, you can still use the
# original name of the function.

# Answer : False

'''
Question 5
'''
# What is the output of this code?
x = 0
for i in range(2,20,3):
    if i % 2 == 0:
        x += 1
print(x)