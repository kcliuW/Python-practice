import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.title('Latex 使用')
plt.text(0.4, 0.6,r"$\int_0^5 f(x)\mathrm{d}x$",fontsize=20,color="blue")
plt.text(0.4, 0.3,r"$\sum_{n=1}^\infty\frac{-e^{2\pi}}{3^n}!$",fontsize=20,color="red")
plt.show()