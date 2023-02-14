# Question 1
def myAdd(x=2,y=4, *args):
    while(x<y):
        for ar in range(len(args)):
            return (x+y+args[ar+2])
            break
print(myAdd(3,4,5,6,9))

# Question 2
def foo(): # locals
    print(globals()==locals()) # False
foo() # globals
print(globals()==locals()) # True

# Question 3
print(1+2+3+4%5) # Note: 4 % 5 = 4 .Therefore 1+2+3+4%5 = 1+2+3+4 = 10

# Question 4
a = [1,2,0,3,4]
for x in range(len(a)):
    if x >= 4:          # Note for x in len(a), that is 5 . x > 4 .Then execute the print
        print(a[-a[-1]])
        print(len(a))
        print(-a[-1])   # (a[-1]) equals to 4, [-a[-1]] equals to -1 * a[-1] = -4
                        # Therefore a[-a[-1]] equals to a[-4] = 2

# Question 5
i = [1,2,3,4]*(-1)
print(i)