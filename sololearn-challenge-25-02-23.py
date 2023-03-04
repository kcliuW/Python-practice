'''Question 1'''
# What is the output of this code?
a = 3
b = 8
c = str(a)+str(b)
print(c)

'''Question 2'''
# Fill in the blank to convert the 
# string into the following list['Hello','world'].

Hello = "Hello world"
print(Hello.split())

'''Question 3'''
variable = 9

def function(variable):
    variable += 1
    print(variable)

function(7)

print(variable)

'''Question 4'''
# What is the output of this code?
def fac(c):
    if c > 0:
        return c * fac(c-1)
    else:
        return 1
print(fac(4))

'''Question 5'''
# What is the output of this code?
a,b,c = 2,7,8
print(a+b*a//c)