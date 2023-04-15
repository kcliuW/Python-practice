'''
Question 1
'''
x = y = 5, 10   # Note : There are two tuples :
                # x tuple & y tuple with the same elements : 5,10 
                # x = (5,10) type tuple, y = (5,10) type tuple

res = x == y    # res is equal to x, which x & y have same elements.
                # x == y , thus return True value
print(res) 

'''
Question 2
'''
list1 = [41, 16, 12, 'a', 'b']
y = [(var*2) for var in list1]              # It will be [82, 32, 24, 'aa', 'bb']
print(y)
result = [(var*2) for var in list1[:-3]]    # Note: list1[:-3] means that -1 to -3 elements excluded
print(result)                               # So, it will be [82, 32]

'''
Question 3
'''
list1 = [11,5,14,6,2,17,1,4]
result = [x**2//2 for x in list1] # type: ignore
print(result)
print(min(result))

'''
Question 4
'''
x = 4
while x < 10:
    x *= x/2    # Note : First x = 4, then x *= x/2 will be 4 * 4/2 , which is 8.
    print(x)    #        Second, x = 8, then 8 * 8/2, which is 32.
print(x)        #        Third, x =32, which is greater than 10, while loop end.

'''
Question 5
'''
lista = [15, 16, 12, 55, 8]
listb = [3, 4]
#lista.extend[listb*2]   # TypeError: 'builtin_function_or_method' object is not subscriptable
lista.extend(listb*2)
print(lista) 
