# ch1_23.py
import matplotlib.pyplot as plt
import numpy as np

xpt = np.linspace(0, 5, 500)
ypt = 1 - 0.5*np.abs(xpt -2)
lwidths = (1+xpt)**2
plt.scatter(xpt, ypt, s=lwidths, color =(0, 1, 0))
plt.show()