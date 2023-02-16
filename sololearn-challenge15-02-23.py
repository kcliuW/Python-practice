# Question 1
# What is the output of this code?
try:
    print(1/0)
except:
    print(1)
print(2)

# Question 2
# What is the output of this code?
a = [1,7,[3,8],9,5]
b = len(a)
c = a[2][0]
x = b % c
print(x)

# Question 3
# What is the output of this code?
class Things:
    def __init__ (self, spots):
        self.spots = spots
bug1 = Things(13)
bug2 = Things(18)
total = bug1.spots + bug2.spots
difference = bug2.spots - bug1.spots
print(total + difference)

# Question 4
# What is the output of this code?
a = set([1,2,3,4])
b = set([1,2,5,6])
x = a & b
print(len(x))

# Question 5
# What is the output of this code?
def func():
    a = print('hello', end= " ")
    return a
c = func()
if c == 'hello':
    print('true')
else:
    print('false')
    