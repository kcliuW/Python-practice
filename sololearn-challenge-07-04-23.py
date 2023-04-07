'''
Question 1
'''
# What is the output of this code?
class Vec:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def __add__(self,other):
        return
#Vec(self.x + other.x, self.y + other.y)
v1 = Vec(3,4)
v2 = Vec(1,2)
r = v1 + v2
#print(r.x + r.y)

# Answer : 10

'''
Question 2
'''
# What is the output of this code?
list = [0,1,2]
for i,v in enumerate(list):
    print(v+i, end='')
    
'''
Question 3
'''
# What is the output of this code?
string = 'abc'
#lst = string.split("")
#print(lst)

# Answer : Error --> ValueError: empty separator for ---> lst = string.split("")

'''
Question 4
'''
# What is the output?
# print("5"+2)
# Answer : Error , invalid type

'''
Question 5
'''
# What is the output?
def fun():
    pass
print(type(fun()))