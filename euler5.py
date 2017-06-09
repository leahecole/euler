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
    a = np.mat(np.arange(1, 21))
    b = np.ones((1, 20))*num
    c = np.mod(b,a)
    d = np.nonzero(c==0)
    if np.size(a[d])>17:
    	print np.size(a[d])
    	print num
    if np.size(a[d]) == 20:
    	return True

    else:
		return False



# i=2520
i = 121474080
cond = False
while(not cond):
	cond = divisibleByTwenty(i)
	i+=19
print i-1


