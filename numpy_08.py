import numpy as np

A = np.arange(4)
B = A
C = A
D = B

A[0] = 11
print(A)
print(B)
print(C)
print(D)#改变关联的任何数值，其他都会改变

E = A.copy()#deep copy 此种赋值不会关联。
