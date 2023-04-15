import matplotlib.pyplot as plt

squares = [0,1,4,9,16,25,36,49,64]
plt.plot(squares, lw = 10)      # 串列 squares 數據是 y 的值, 線條寬度是 10
plt.axis([0, 8, 0, 70])         # x 軸刻度 0-8, y 軸刻度 0-70
plt.grid()
plt.show()  