# ch6_1_2.py
from sympy import Symbol, solve

x = Symbol('x') # type: ignore
y = Symbol('y') # type: ignore
z = Symbol('z') # type: ignore
eq1 = 2 * x - 4 * y + 1 * z + 9 # type: ignore
eq2 = 4 * x + 2 * y - 3 * z - 17
eq3 = 1 * x - 1 * y + 5 * z + 11
ans = solve((eq1, eq2, eq3))
print(type(ans))
print(ans)
print('x = {}'.format(ans[x]))
print('y = {}'.format(ans[y]))
print('z = {}'.format(ans[z]))