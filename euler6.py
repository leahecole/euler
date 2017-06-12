import numpy as np

num = 100

a = np.mat(np.arange(1, num+1))
b = np.transpose(a)
c = a*b
d = np.sum(a)**2
print c
print d
print d-c

