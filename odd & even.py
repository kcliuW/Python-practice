a = int(input("Please enter the number1: "))
b = int(input("Please enter the number2: "))

def is_even(x):
    if x == 0:
        return True
    else:
        return is_odd(x-1)

def is_odd(x):
    return not is_even(x)

print(is_odd(a))
print(is_even(b))