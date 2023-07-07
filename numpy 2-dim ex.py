import numpy as np

grades = np.array([[95,100,100],[86,90,75],[98,98,96],[78,90,80],[70,68,72]])
print(grades)

x = grades[0,]
print(x)

y = grades[0,0]
print(y)

z = grades[1,2]
print(z)

A = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(A)

B = np.array([1,2,3,4,5,6,7,8,9,10,11,12]).reshape(4,3) # change to 2-dim matrix
print(B)

C = np.arange(15).reshape(3,5) # est. 3x5 2-dim matrix
print(C)

D = np.linspace(0,2,9).reshape(3,3) # est 3x3 2-dim matrix
print(D)

H = np.array([1,2,3,4,5,6,7,8,9,10,11,12]).reshape(4,3)
print(H)

print(H.ndim)
print(H.shape)
print(H.shape[0])
print(H.shape[1])
print(H.size)
print(H.dtype)
print(H.itemsize)

print('\n')
print(H[0,0])
print(H[0,:])   # First row elements, A[0,] or A[0]
print(H[:,0])   # First column elements
print(H[1:3,0]) # First column elements A[1,0] & A[2,0] (excluded A[3,0])
print(H[2:])    # Third row elements
print(H[:2])    # First & Second row elements
print(H[-1])    # Last row elements

for i in H:
    print(i + 10)
    
X = np.array([[1,2],[3,4]])
Y = np.array([[2,2],[1,1]])

print(X*2)
print(X>2)
print(X+Y)
print(X-Y)
print(X*Y)
print(X/Y)

X[0,0] = 7 # Change 1st row 1st column element to 7
print(X)