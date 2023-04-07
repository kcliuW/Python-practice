'''
Question 1
'''
# What is the output of this code?
a = [1,2,3,4]
b = a.copy()
print(b)
b.append(a) # it equals to [1,2,3,4,[1,2,3,4]].That is len(b) is 5 # type: ignore
print(b)
a.append(b) #  it equals to [1,2,3,4,[1,2,3,4,[...]]]. That is len(a) is 5 # type: ignore
print(a)
print(len(a)*len(b))

'''
Question 2
'''
# What is the output of this code?
first = lambda y, x : x * y         # first(2,1) = 2*1 = 2
second = lambda x, y : x + y        # second(first(2,1),2) = 2*2 = 4
string_mult = second(first(2,1),2)  # Therefore, string_mult = 4
chars = string_mult * "a"           # chars = 4 * "a" = "aaaa"
print(len(chars))
print(chars)

'''
Question 3
'''
# What is the output of this code?
print('x' in set('xray'),
'xray' in['xray','doctor','nurse'])

'''
Question 4
'''
# What is the output of this code?
print(6+5-4*3/2%1) # First, calculuate 4*3/2%1 = 0.0. Second, 6+5 - 0.0 = 11.0

'''
Question 5
'''
# What is the output of this code?
x = 5
while x >= 0:
    x = x-1
    print(x)
print(x)