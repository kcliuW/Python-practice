# ch1_22.py
import matplotlib.pyplot as plt
import numpy as np

left = -2 * np.pi
right = 2 * np.pi
x = np.linspace(left, right, 100)

f1 = 2 * np.sin(x)
f2 = np.sin(2*x)
f3 = 0.5 * np.sin(x)
f4 = np.sin(x)

plt.plot(x, f1, label = '2sin(x)')
plt.plot(x, f2, label = 'sin(2x)')
plt.plot(x, f3, label = '1/2sin(x)')
plt.plot(x, f4, label = 'sin(x)')
plt.legend(loc = 1)
plt.show()