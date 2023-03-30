'''
Question 1
'''
#What is the output of this code?
my_list = ["car","plane","train","bike","rocket"]
new_list = sorted(my_list,key=lambda x: x[-2])
print(new_list)

'''
Question 2
'''
#What is the output of this code?
print(-15//10.0)

'''
Question 3
'''
# Function can receive an array as a parameter.°
# Answer : True•

'''
Question 4
'''
#What is the output of this code?
a = [0, 57, 28]
a.sort(reverse=True)
print(a[2])

'''
Question 5
'''
#What is the output of this code?
class A:
 x = 1
 def __add__(self,obj):
     if isinstance(obj,A):
         return self.x + obj.x
     return "False"
class B(A):
    x = 2
a = A()
b = B()
print(a + b)