# ch1_19.py
import matplotlib.pyplot as plt

xpt = list(range(1, 101))
ypt = [x**2 for x in xpt]
plt.axis([0, 100, 0, 10000])
plt.scatter(xpt, ypt, color=(0,1,0))
plt.show()