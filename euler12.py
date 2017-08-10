import numpy as np
import time

#returns nth triangle number (adds up all previous natural numbers)
def triangle(number):
	
	return (number*(number+1))/2

# #brute force - test all numbers less than that
# def divisibleByN(num):
#     a = np.mat(np.arange(1, num+1))
#     b = np.ones((1, num))*num
#     c = np.mod(b,a)
#     d = np.nonzero(c==0)
#     if np.size(a[d]) > 500:
#     	return True
#     else:
#     	if np.size(a[d]) > 100:
#     		print num
#     		print np.size(a[d])
#     	return False

#from Stackoverflow
def primes_upto(limit):
    prime = [True] * limit
    for n in range(2, limit):
        if prime[n]:
            yield n # n is a prime
            for c in range(n*n, limit, n):
                prime[c] = False # mark composites

#go through, if divisible by it
#take that answer, and break it down to prime factor

def primeFactors(num, mults):
    b = np.ones((1, np.size(mults)))*num
    #does modular division to see which divide evenly
    c = np.mod(b, mults)
    d = np.nonzero(c==0)
    p = mults[d]

    #p is which ones divide evenly
    #we want to know how many divide evenly though


    return mults[d]


def findDivisors(n, primes):
	p = primeFactors(n, np.mat(primes))
	p = p.tolist()[0]
	for i in p:
		print "i", i
		print n/i






start = time.clock()
primes = list(primes_upto(1000000))

satisfied = False
i = 1
while not satisfied and i<20:
	j = triangle(i)
	if j < 1000000:
		print j
		satisfied = findDivisors(j, primes)
	else:
		print "not enough primes"
		break
	i+=1
fin = time.clock()
print fin-start
