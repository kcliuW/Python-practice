from sympy import Symbol
from sympy.plotting import plot
x = Symbol('x')
line = plot(2*x-5, 3*x+2, legend = True, show = False)
line[1].line_color = 'r'
line.show()