# ch1_32.py
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]

votes = [135, 412, 397]
N = len(votes)
x = np.arange(N)
width = 0.35
plt.bar(x, votes, width)

plt.ylabel('票數')
plt.title('選舉結果')
plt.xticks(x, ('James', 'Peter', 'Norton'))
plt.yticks(np.arange(0, 450, 30))
plt.show()
