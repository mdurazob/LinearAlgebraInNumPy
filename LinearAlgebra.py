import numpy as np
import array_to_latex as a2l

x = np.array([[1, 2], [4, 5]])
y = np.array([[2, 6], [4, 4]])

## Copia la array a clipboard
a2l.to_clp(x, frmt = '{:6.2f}', arraytype = 'array')

print(x)
print(y)
print(np.add(x, y))
#  add()is used to add matrices
print("Addition of two matrices: ")
print(np.add(x, y))
# subtract()is used to subtract matrices
print("Subtraction of two matrices : ")
print(np.subtract(x, y))
# divide()is used to divide matrices
print("Matrix Division : ")
print(np.divide(x, y))
print("Multiplication of two matrices: ")
print(np.multiply(x, y))
print("The product of two matrices : ")
print(np.dot(x, y))
print("square root is : ")
print(np.sqrt(x))
print("The summation of elements : ")
print(np.sum(y))
print("The column wise summation  : ")
print(np.sum(y, axis=0))
print("The row wise summation: ")
print(np.sum(y, axis=1))
# using "T" to transpose the matrix
print("Matrix transposition : ")
print(x.T)
