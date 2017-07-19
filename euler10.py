def primes_upto(limit):
    prime = [True] * limit
    for n in range(2, limit):
        if prime[n]:
            yield n # n is a prime
            for c in range(n*n, limit, n):
                prime[c] = False # mark composites

primes = list(primes_upto(2000000))
sum = 0
for x in primes:
	sum+=x

print sum