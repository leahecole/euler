import numpy as np

def divisibleByTen(num):
    a = np.mat(np.arange(1, 11))
    b = np.ones((1, 10))*num
    c = np.mod(b,a)
    d = np.nonzero(c==0)
    if np.size(a[d]) == 10:
    	return True

    else:
		return False

def divisibleByTwenty(num):
    # a = np.mat(np.arange(1, 21))
    b1 = [11, 13, 14, 17, 18, 19, 20]
    a = np.mat(b1)
    b = np.ones((1, np.size(a)))*num
    c = np.mod(b,a)
    d = np.nonzero(c==0)
    e = np.size(a[d])

    if e > 5:
    	print e
    	print num
    if e == 7:
    	return True

    else:
		return False



# i=2520
i=20
cond = False
while(not cond):
	cond = divisibleByTwenty(i)
	i+=20
print i-1


