from sympy import Symbol
x = Symbol('x') # type: ignore
y = Symbol('y') # type: ignore
eq = 5 * x + 6 * y
result = eq.subs({x:1, y:2})
print(result)