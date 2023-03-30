# Question 1
a = 8
b = 4
c = a/b
d = str(c)
print(2*d)

# Question 2
import math
print(math.factorial(4))

# Question 3
it = iter('abcdef')
for i in range(3,6):
    print(next(it), end ="\n")

# Question 4
j = 2
while j <= 19:
    print(j+5)
    j*=7
# Note : a) 1st number is 2 + 5 = 7. b) 2nd number is 2*7 + 5 = 19. Therefore, the answer is 7, 19

# Question 5
print((lambda x:x**2*x)(5))