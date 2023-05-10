from sympy import solve, Symbol
x = Symbol('x') # type: ignore
eq = 3*x + 5 - 8
result = solve(eq)
print(result)
print(type(result))