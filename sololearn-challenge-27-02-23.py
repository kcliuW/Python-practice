'''Question 1'''
# How many times will the string
#"loop" be printed?

arr = [0, 1, 2, 3, 4, 5]
n = 0
for _ in arr:
    del arr[n]
    n += 1
    print("loop")
    
'''Question 2'''
# What is the output of this code?
print('abcde'[::-1])

'''Question 3'''
# What is the output of this code?
print((2**3)**2)

'''Question 4'''
# What is the output of this code?
a = [0]
def func(x):
    x[0] = 1
func(a)
print(a)

'''Question 5'''
# What is the output of this code?
x,y,z = 2,3,1
print('x:{0},y:{1},z:{2}'.format(z,x,y))