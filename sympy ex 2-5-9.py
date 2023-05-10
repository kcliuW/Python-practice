from sympy import solve, symbols
x, a, b, c = symbols('x, a, b, c')
eq = a*x*x + b*x + c
ans = solve(eq, x)
print(ans)