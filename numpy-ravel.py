'''
numpy中的ravel()、flatten()、squeeze()的用法與區別
'''

# numpy 中的ravel()、flatten()、squeeze()都有將多維數組轉換為一維數組的功能，區別：
# ravel()：如果沒有必要，不會產生源數據的副本
# flatten()：返回源數據的副本
# squeeze()：只能對維數為1的維度降維

# 另外，reshape (-1)也可以“拉平”多維數組

import numpy as np
arr = np.arange(12).reshape(3,4)
print(arr)

a = arr.ravel()
print(a)

b = arr.flatten()
print(b)

z = arr.reshape(-1)
print(z)

x = np.arange(3).reshape(3,1)
print(x)

y = np.squeeze(x)
print(y)