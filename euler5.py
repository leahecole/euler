import numpy as np

def divisibleByTen(num):
    a = np.mat(np.arange(1, 11))
    b = np.ones((1, 10))*num
    c = np.mod(b,a)
    print a
    print b
    print c


divisibleByTen(2050)
