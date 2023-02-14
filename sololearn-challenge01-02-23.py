# Question 1
P,q,*r = [y for y in range(0,16,4)if y % 4 == 0]
print(r)

# Question 2
a = [1,6,5,8,9,0]
print(a[2]+a[5])

# Question 3
'''import numpy
arr = numpy.arrange(3,15,3)
print(arr[2])'''

# Question 4
a = {1,2,3}
a.add(0)
print(len(a))

# Question 5
x = [i for i in range(11) if i%2 == 0]
n = 0
for j in x:
    n += j
print(n)