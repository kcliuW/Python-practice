# Question 1
# What is the output of this code?
a = 1
b = 3
if (a <= 5 and b < 9):
    if (a == 4):
        b = 20
    a += 1
    b -= 1
if (b <= 20):
    a = -5
print(a)


# Question 2
# How many numbers does the list contain after this code ?
a = []
for i in range(1,10):
    if (i % 2 == 0) or (i % 3 == 0):
        a.append(i)
        print(a)


# Question 3
# What is the output of the code below?
a = [0, 3, 5, 8]
b = (1, 7, 9, 6)
c = {2: 6, 4: 8}
print(a[2], b[2], c[2])


# Question 4
# What is the output of this code?
i ='3471'
z = i[::-1]
if i == z:
    print(z)
else:
    print(z[2]* 2 + z[3]* 2)

# Question 5
# What is the output of this code?
print('My name is Khans'.split(sep=' ', maxsplit = 1))
