import numpy as np
U = np.array([1,2,3])
V = np.array([1,0,1])

A = np.inner(U,V) # np.dot(U,V). U.V = u1v1 + u2v2 + u3v3
print(A)

B = np.cross(U,V) # np.cross(U,V). U.V = (u2v3 - u3v2, u3v1 - u1v3, u1v2 - u2v1)
print(B)

C = np.outer(U,V) # np.outer(U,V). U.V = [u1v1 u1v2 u1v3]
              #                          [u2v1 u2v2 u2v3]
              #                          [u3v1 u3v2 u3v3]
print(C)