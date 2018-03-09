import numpy as np


A = np.arange(3,15).reshape((3,4))
print(A)
print(A[2])#取第三个数或第三行
print(A[1][1])#索引准确位置也可以A[1,1]表示 
print(A[:,1])#第一列的所有数，：用法和python中一样

for row in A:
    print(row)#迭代每一行

for column in A.T:
    print(column)#没有迭代列的方法，通过迭代倒置矩阵的行就是列

for item in A.flat:
    print(item)#A.flatten()可以把矩阵变成一维，这样可以迭代矩阵中每一个值

