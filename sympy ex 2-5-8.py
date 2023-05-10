from sympy import solve, Symbol
x = Symbol('x') # type: ignore
eq = x**2 + 5*x
ans = solve(eq)
print(ans)
print(ans[0])
print(ans[1])