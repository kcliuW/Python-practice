'''
Question 1
'''
# Which of the following function
# converts a string to a float?

# Answer: float(x)

'''
Question 2
'''
# What is the output of this code?
y=[x for x in range(10) if x//3 == 2] # x//3 == 2, i.e 6, 7, 8. Therefore, sum is 21.
print(sum(y))

'''
Question 3
'''
# Fill in the blank to print 'world'.

word = ['Hello','world','!']
num = 4 % 3     # Because the index of 'world' is 1, and num = 4 % 3 equals to 1
print(word[num])

'''
Question 4
'''
# What is the output of this code?
list = [2,3,6]
#list.append(5,4) # error , append() only contain one argument
#print(list1[3]) # there is no list1, only list,even the [3] is out of range.

'''
Question 5
'''
# What is the output of this code?
a,b = 1,1
a,b = b + a, a
c = a + b
print(c)
