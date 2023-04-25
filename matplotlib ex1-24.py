# ch1_24.py
import matplotlib.pyplot as plt
import numpy as np

left = -np.pi
right = np.pi 
x = np.linspace(left, right, 100)
y = np.sin(3*x)

plt.plot(x, y)
plt.fill_between(x, 0, y, color='green', alpha=0.1)
plt.show()
