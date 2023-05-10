from sympy import Symbol
x = Symbol('x') # type: ignore
a= x + x + 2 # type: ignore
print(a)
print(x.name) # type: ignore

y = Symbol('x')
b = y + y + 2
print(b)
print(y.name)