from sympy import solve, symbols
x, y = symbols('x, y')
eq1 = 3*x + 2*y - 6
eq2 = 9*x + y - 3
ans = solve((eq1, eq2))
print(ans)
print('x is equal to:',ans[x])
print('y is equal to:',ans[y])
