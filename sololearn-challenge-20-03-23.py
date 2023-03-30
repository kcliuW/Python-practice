'''
Question 1
'''
# What is the output of this code?
a = [4,2,6,1]
print(a.sort())
print(a)

'''
Question 2
'''
# What is the output of this code?
list = [1,2,3,4]
if list [3] == 3:
    print(list[1])
else:
    print(list[3])

'''
Question 3
'''
# What is the output of this code?
a = [1,2,3,4,5]
del a[0]
print(a[1])

'''
Question 4
'''
# What is the output of this code?
x = 0
for i in range(2,20,3):
    if i % 2 == 0:
        x += 1
print(x)

'''
Question 5
'''
# What is the output of this code?
a = [0,1,2,3]
a[:] = [sum(a)]
print(len(a))
print(a)