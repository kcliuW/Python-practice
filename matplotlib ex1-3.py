import matplotlib.pyplot as plt

squares = [0,1,4,9,16,25,36,49,64]
plt.plot(squares)       # 串列 squares 數據是 y 的值
plt.axis([0, 8, 0, 70]) # x軸刻度 0-8, y軸刻度 0-70
plt.grid()
plt.show() 