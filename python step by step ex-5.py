# Lesson review ex

# Q.7
i = 1
while i < 200:
    i += 5
print(i)

# Q.8
total = 0
count = 0
while count <= 21:
    total += count
    count += 7
print(total)

# Q.9
a = 100
n = 0
while a >= 0:
    n += 1
    a -= n
print(n)    # 100 依次減去 1,2,3... 直到 n 時, 相減的結果為負.
print(a)    # 100 依次減去 1,2,3... 直到 13 時, 相減的結果是 9. 所以減去 14 時, 結果為 -5.

'''
Question 3
'''

for a in range(1,4):
    for b in range(1, a+3):
        if b == 3:
            break
        print(b, end="")
    print()

'''
Question 4
'''

for x in range(1, 12, 2):
    if x == 5:
        continue
    print(x, end="")
    
'''
Question 5
'''

for x in range(1, 12, 2):
    if x == 5:
        break
    print(x, end="")
    
'''
Question 6
'''
x = "aeiou"
for i in x:
    print(i, end='')

'''
Question 7
'''
x =['Happy', 'New', 'Year']
for i in x:
    print(i,end=' ')

'''
Question 8
'''
for x in range(1,11,3):
    print(x, end=' ')
print()

'''
Question 9
'''
n = 109658574
while n!=0:
    print("%d"%(n%10), end='')
    n//=10

'''
Question 10
'''
fac = 1
for i in range(1, 11):
    fac *= i
print(fac)

'''
Question 12
'''
x = "13579"
for i in x:
    print(i, end='')

'''
Question 13
'''
product = 1
for i in range(1,11,3):
    product *= i
print(product)

'''
Question 14
'''
n = 53179
while n != 0:
    print("%d" %(n%10), end='')
    n //= 10

'''
Quiz 1
'''

list1 = ['b', 12, 4, 'a']
list2 = ['i','ii','iii','iv']
result = zip(list1,list2)
print(dict(result))

'''
Quiz 2
'''

import numpy as np

a = np.array([1,2,3,4])
b = np.array([3,4,5,6])
c = np.intersect1d(a,b)
print(c.sum())

'''
Quiz 3
'''
a = 20
def increase(c):
    b = 1
    while b <= 5:
        print(b, c)
        c = c + 10  # b = 1, c = 20. b = 2, c = 30. b = 3, c = 40. b = 4, c = 50. b = 5, c = 60.
        b = b + 1
increase(a)