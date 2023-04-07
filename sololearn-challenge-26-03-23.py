'''
Question 1
'''
# Select the correct printed result.

s = {10, 20, 30}
t = {3, 4}
u = s.union(t)
print(u)

# u = s.union_update(t) --> No this union_update() Therefore, u equal to nothing

'''
Question 2
'''
# What is the output of this code?
a = [(1,0),[2,3,1],{1:'a', 4:'b'}]
lst = []
for n in a:
    lst.extend(n)
print(len(lst))
print(lst)

'''
Question 3
'''
# Code inside of an if statement
# needs to be indented.

# Answer : True

'''
Question 4
'''
# What is the output of this code?
a = 10
b = 2
c = (b % a)**(a % b)
myList = [ c * 2, c * 3]
s = myList[0] + myList[1]
print(s)

'''
Question 5
'''
# What is the output of this code?
def f (x = 0):
    y = x
    def g(y):
        print(y)
    print(x)
    return g
f()(1)