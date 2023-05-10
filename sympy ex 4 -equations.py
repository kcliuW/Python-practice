from sympy import solve, symbols
a, b, c, d = symbols('a, b, c, d')
eq1 = a + b + c - 2
eq2 = b + c + d + 1
eq3 = c + d + a - 5
eq4 = d + a + b + 3
ans = solve((eq1, eq2, eq3, eq4))
print(ans)
print('a is equal to:',ans[a])
print('b is equal to:',ans[b])
print('c is equal to:',ans[c])
print('d is equal to:',ans[d])