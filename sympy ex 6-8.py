# ch6_8.py
import matplotlib.pyplot as plt
from sympy import Symbol, solve
import numpy as np

x = Symbol('x') # type: ignore
y = Symbol('y') # type: ignore
eq1 = 0.5 * x - y - 0.5
eq2 = - 2 * x - y + 7
ans = solve((eq1, eq2))
print('x = {}'.format(ans[x]))
print('y = {}'.format(ans[y]))

line1_x = np.linspace(-5, 5, 10)
line1_y = [(0.5 * y - 0.5) for y in line1_x]
line2_x = np.linspace(-5, 5, 10)
line2_y = [(- 2 * y + 7) for y in line2_x]

plt.plot(line1_x, line1_y)
plt.plot(line2_x, line2_y)

plt.plot(ans[x], ans[y], '-o')
plt.text(ans[x] - 0.7, ans[y] + 0.5, '('+str(int(ans[x]))+','+str(int(ans[y]))+')')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid()
plt.axis('equal')
plt.show()