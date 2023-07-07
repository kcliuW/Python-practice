import numpy as np

a = np.array([1,2,3])
print(type(a))
print(a)
print(a*3)
print(a+2)

g = [1,2,3] * 3     # list
print(g)

b = np.array([2,2,0])
print(a+b)
print(a/b)
print(a*b)

c = np.arange(10)
print(c)

d = np.arange(0,10,2)
print(d)

e = np.linspace(0, 10, 15)
print(e)

A = np.array([10, 20, 30])
print(A)

H = np.array([1,3,5,7,9,0])
print(H.ndim)
print(H.shape)
print(H.size)
print(H.dtype)
print(H.itemsize)

B = np.array([1.2, -3.5, 7.6, 3.2, 8.8])
print(B.dtype)

C = np.array(["coffee", "tea", "cola"])
print(C.dtype)

D = np.arange(1,10,3)
print(D)

E = np.arange(5)
print(E)

F = np.arange(0,2,0.3)
print(F)

G = np.linspace(0,2,9)
print(G)

