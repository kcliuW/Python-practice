'''Question 1'''
# What is the output of the following code?
t = (1,2,[3,4])
'''t[2,0]=5'''
'''print(t)''' # Result : TypeError: 'tuple' object does not support item assignment

'''Question 2'''
# What is the output of this code? # ALDN -- 116
a = [2,4,5]
for i in range(1,3):
    a[i] = a[i - 1]
    print(a[i], end ="")

'''Question 3'''
# What is the output of this code?
list1 = []
list2 = []
list3 = []
for i in range(5)[::-1]: # Reversed list of [0,1,2,3,4] to [4,3,2,1,0]
    list1.append(i)      # list 1 append the result of range(5)
for j in list1[::-2]:    # Reversed list1 of [4,3,2,1,0] to [0,2,4]
    list3.append(j)      # lists 3 append the result of j
    list2.append(j + 1)  # list2 append j + 1 result [0,2,4] to [1,3,5]
print(list1[2])
print(list1)
print(list3)
print(list2)

'''Question 4'''
# What is the output of this code?
x ="".join(["1","2"]*2)
print(x)

'''Question 5'''
# What is the output of this code?
a = 10
b = 2
c = (b % a) ** (a % b) # Note (b % a) = 2, (a % b) = 0. Therefore, c = 2**0 = 1
myList = [c * 2, c * 3]
s = myList[0] + myList[1]
print(s)
