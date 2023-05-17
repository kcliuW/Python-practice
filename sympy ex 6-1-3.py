# ch_6-1-3.py
# ch6_1_2.py
from sympy import Symbol, solve

x = Symbol('x') # type: ignore
y = Symbol('y') # type: ignore
z = Symbol('z') # type: ignore
eq1 = b * x + a * y + 0 * z - c # type: ignore
eq2 = c * x + 0 * y + a * z - b # type: ignore
eq3 = 0 * x + c * y + b * z + a # type: ignore
ans = solve((eq1, eq2, eq3))
print(type(ans))
print(ans)
print('x = {}'.format(ans[x]))
print('y = {}'.format(ans[y]))
print('z = {}'.format(ans[z]))