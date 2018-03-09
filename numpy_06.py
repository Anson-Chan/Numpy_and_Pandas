import numpy as np

A = np.array([1,1,1])[:,np.newaxis]
B = np.array([2,2,2])[:,np.newaxis]

C = np.vstack((A,B)) #vertical stack上下合并
D = np.hstack((A,B)) #horizontal stack左右合并

print(C)
print(D)

print(A[:,np.newaxis])#在原array前加了维度，类似（3,）变成了（1,3）

E = np.concatenate((A,B,B,A),axis=0)#此种合并相比上种方法可以进行三个以上合并，并且可以定义axis在横向和纵向进行合并
print(E) 
