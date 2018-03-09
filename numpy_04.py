import numpy as np

A = np.arange(2,14).reshape((3,4))

print(A)
print(np.argmin(A))#表示输出最小值所在位置的索引，同理最大值索引argmax()
print(np.mean(A))#求平均值，另一种表现形式A.mean()，可以指定axis分别对行和列求平均值
print(np.median(A))#求中位数
print(np.cumsum(A))#求累加值，第几个就是前几个数的累加
print(np.diff(A))#求相邻两位的差，同样以矩阵的形式输出
print(np.nonzero(A))#输出非零位置
print(np.sort(A))#逐行进行排序
print(np.transpose(A))#矩阵倒置
print((A.T).dot(A))#矩阵倒置与矩阵本身相乘
print(np.clip(A,5,9))#输入一个最小值一个最大值，把小于最小值的数替换成最小值，大于最大值替换成最大值
