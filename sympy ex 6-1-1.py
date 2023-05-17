# ch6_1_1.py
from sympy import Symbol, solve

a = Symbol('a') # type: ignore
b = Symbol('b') # type: ignore
c = Symbol('c') # type: ignore
eq1 = a + 2 * b + 3 * c # type: ignore
eq2 = 4 * a + 5 * b + 6 * c
eq3 = 7 * a + 8 * b + 9 * c
ans = solve((eq1, eq2, eq3))
print(type(ans))
print(ans)
print('a = {}'.format(ans[a]))
print('b = {}'.format(ans[b]))
print('c = {}'.format(ans[c]))