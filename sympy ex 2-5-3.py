from sympy import Symbol
# a = Symbol('a')
# b = Symbol('b')
# c = Symbol('c') or

from sympy import symbols
a, b, c = symbols('a,b,c')
print(a.name)
print(b.name)
print(c.name)

x = Symbol('x') # type: ignore
y = Symbol('y') # type: ignore
z = 5 * x + 6 * y + x * y
print(z)