import numpy as np


a = np.array([10,20,30,40])
b = np.arange(4)


print(a,b)
c = b**2
#c = 10*np.sin(a) #同理cos() tan()
print(c)

print(b)
print(b<3)#判断b中小于三的值

d = np.array([[1,1],
              [0,1]])
e = np.arange(4).reshape((2,2))
f = d*e
d_dot = np.dot(d,e)#两矩阵相乘
print(f)
print(d_dot) 

a1 = np.random.random((2,4))

print(a1)
print(np.sum(a1,axis=1))#axis是行和列 0是行，1是列，表示在行和列中求值
print(np.min(a1))
print(np.max(a1))
