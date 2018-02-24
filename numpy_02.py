import numpy as np


a = np.array([2,23,4], dtype=np.int) #这里np.int是格式(dtype)，比如int32,int64,float
b = np.zeros((3,4)) #生成一个三行四列的全是0的矩阵
#b = np.ones((3,4)) #生成全是....1
#b = np.empty((3,4))

c = np.arange(10,20,2) #从10开始，生成相隔2的数组。
#c = np.arange(12).reshape((3,4))  #reshape 重新定义数组维度，里面装填1-11之间的数

d = np.linspace(1,10,20).reshape((4,5)) #在1-10数字间生成20段线段,用reshape重新定义维度。


print(a)
print(b)
print(c)
print(d)
