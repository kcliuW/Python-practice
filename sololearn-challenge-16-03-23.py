'''
Question 1
'''
# What is the output of this code?
A = ['a','b', (), []]
print(len(A))

'''
Question 2
'''
# What is the output of this code?
print(True or False and False)
print((True or False)and False)
print(False and False or True)

'''
Question 3
'''
# What is the output of this code?
x = 5
if x > 0:
    x = x + 1
print(x)

'''
Question 4
'''
# What is the output of this code?
vals = [2,4,7]
news = "{1}{2}{1}".format(vals[0],vals[2],vals[1])
print(news)

'''
Question 5
'''
# What is the output of this code?
r = ['red','orange','yellow','green','blue','indigo']
p = [c[0] for c in r if len(c) < 6] # p equals to character in r if the length of character < 6
print(''.join(p))