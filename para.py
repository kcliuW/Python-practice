def factorial(*arg): # *arg means more than 1 argument, return value as "Tuple"
    product = 1
    for n in arg:
        product *= n
    return product

ans1 = factorial(5)
print(ans1)
ans2 = factorial(5,4)
print('5*4=', ans2)
ans3 = factorial(5,4,3)
print('5*4*3=', ans3)
ans4 = factorial(5,4,3,2)
print('5*4*3*2=', ans4)

def myfruit(**arg):  # **arg means more than 1 argument, return value as "Dictionary"
    return arg
print(myfruit(d1='apple', d2='mango', d3='grape'))