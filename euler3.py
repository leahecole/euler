import numpy as np
num = 600851475143
# num = 100
#from Stackoverflow
def primes_upto(limit):
    prime = [True] * limit
    for n in range(2, limit):
        if prime[n]:
            yield n # n is a prime
            for c in range(n*n, limit, n):
                prime[c] = False # mark composites

primes = list(primes_upto(1000000))
#go through, if divisible by it
#take that answer, and break it down to prime factor

def primeFactors(num, mults):
    b = np.ones((1, np.size(mults)))*num
    c = np.mod(b, mults)
    d = np.nonzero(c==0)
    return mults[d]


print primeFactors(num, np.mat(primes))
