# ch5_1.py
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1000, 100)
y = 0.03 * x - 18
plt.axis([0, 1000, -20, 15])
plt.plot(x,y)
plt.xlabel("Customers")
plt.ylabel("Profit")
plt.grid()
plt.show()