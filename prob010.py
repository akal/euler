# sum of all the primes below 2,000,000
from common.primes import primes_func

primes = primes_func()

sum = 0
for p in primes:
    if p >= 2000000:
        break
    sum += p
print sum


