# Question 1
Kimi = "haha"
Jim = "git"
print(Kimi + Jim)

# Question 2
x = [1, 2, 3]
def gen(x):
    a = 42
    x[1] = 42
    x = a
gen(x)
print(x)

# Question 3
A = 12
B = 3
x = A%B
print(x)

# Question 4
def func(x):
    if len(x) < 2:
        return x
    else:
        return x[0] + func(x[1:])
print(func("sololearn"))

# Question 5
def sup( a = 2, b = 2):
    a,b = b,a
    result = a**b
    return result
print([sup(2,3), sup()][::-1])


