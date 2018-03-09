import numpy as np

A = np.arange(12).reshape((3,4))
print(A)


print(np.split(A,2,axis=1))#对 A进行（对象，分割次数，分割方向）注意不能进行不等的分割
print(np.array_split(A,3,axis=1))#可以进行不等的分割
print(np.vsplit(A,3))#横向分割
print(np.hsplit(A,2))#纵向分割
