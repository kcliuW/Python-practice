# ch1_21.py
import matplotlib.pyplot as plt
import numpy as np

xpt = np.linspace(0, 10, 500)
ypt1 = np.sin(xpt)
ypt2 = np.cos(xpt)
plt.scatter(xpt, ypt1, color=(0, 1, 0))
plt.scatter(xpt, ypt2)
plt.show()