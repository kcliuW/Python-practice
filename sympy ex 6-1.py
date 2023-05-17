# ch6_1.py
from sympy import Symbol, solve

a = Symbol('a') # type: ignore
b = Symbol('b') # type: ignore
eq1 = a + b - 1 # type: ignore
eq2 = 5 * a + b - 2
ans = solve((eq1, eq2))
print(type(ans))
print(ans)
print('a = {}'.format(ans[a]))
print('b = {}'.format(ans[b]))