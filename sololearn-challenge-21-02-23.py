''' Question 1 '''
# What is the output of this code?
class R2Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
def dot(a,b):
    return a.x*b.x + a.y*b.y
a = R2Vector(3,2)
print(dot(a, R2Vector(-2,3)))

'''Question 2'''
# What is the output of this code?
x = 7
x += x + 2
print(x)

'''Question 3'''
# What is the output of this code?
rabbit = 10
rabbit += 5
carrot = 1 if rabbit > 10 else 0
carrot -= 1
print(carrot)

'''Question 4'''
# What is the output of this code?
#def func(named_args,*args):
#   print(named_args)
#   return *args
#func(1,2,3,4,5) # answer is error

'''Question 5'''
# What is the output of this code?
def f(q, mylist = []):
    mylist = mylist + q
    return mylist
a = [1]
print(f(a))
a = [2]
print(f(a))