from sympy import Symbol
from sympy.plotting import plot
x = Symbol('x')
plot((2*x-5),(x, -5, 5), title = 'Sympy', xlabel='x', ylabel='2x-5')