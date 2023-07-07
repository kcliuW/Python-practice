import numpy as np

A = np.array([10,20,30,40,50])
B = np.array([1,2,3,4,5])

print(A * 2)
print(A ** 2)
print(A < 35)
print(A + B)
print(A - B)
print(A * B)
print(A / B)
print(A > B)

A[0] = 100
print(A)

A[[0,1]] = 70
print(A)

C = np.insert(A, 1, 100)
print(C)

A[0] = 10

D = np.insert(A,[1,3],7)
print(D)

E = np.delete(A, 2)
print(E)

F = np.delete(A, [1,3])
print(F)

H = np.array([1,2,3])
K = np.array([4,5])
I = np.concatenate((H,K))
print(I)
J = np.concatenate((H,[10,20]))
print(J)