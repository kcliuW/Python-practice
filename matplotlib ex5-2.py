# ch5_2.py
import matplotlib.pyplot as plt
x = [x for x in range(0, 11)]
y = [(3 * y -18) for y in x]
plt.xticks(x)
plt.axis([0, 10, -20, 15])
plt.plot(x,y, '-*')
plt.xlabel("children")
plt.ylabel("Apple")
plt.grid()
plt.show()