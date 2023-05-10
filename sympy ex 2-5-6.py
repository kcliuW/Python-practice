from sympy import sympify
from sympy import Symbol
x = Symbol('x') # type: ignore
eq = input('請輸入公式 : ')
print(eq)
eq = sympify(eq)
a = 2 * eq
print(a)
result = eq.subs({x:1})
print(result)