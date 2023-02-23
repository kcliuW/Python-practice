'''Question 1'''
# What is the output?
a,b,*c = [x for x in range(0,12,3)]
print(*c)

'''Question 2'''
# What is the output of this code?
a = 3
def sumofsum(*nums):
    return sum(nums)
print(sumofsum(a,a**a, a*4))

'''Question 3'''
# What is the output of this code?
var = '131231323568132513'
print(var.count("13"))

'''Question 4'''
strList = ['1','2','3','4','a']
intList = []
for i in strList:
    try:
        intList.append(int(i))
    except ValueError:
        intList = ['Something Not Int']
    finally:
        intList = []
print(str(len(intList)))

'''Question 5'''
# What is the output of this code?
a = [0,1,0]
b = [1,1,0]
s = 0
for x in (a,b,a):
    s += x.count(1)
print(s)