import math
import itertools
from bisect import bisect_left

def primes_func():
    yield 2
    ps = [2]
    num = 3
    while True:
        lim = int(math.sqrt(num))
        is_prime = True
        for p in ps:
            if p > lim:
                break
            if num % p == 0:
                is_prime = False
        if is_prime:
            ps.append(num)
            yield num
        num += 1

def prime_factors(num):
    pf = []
    while True:
        if num == 1:
            return pf
        primes = primes_func()
        for p in primes:
            if num % p == 0:
                pf.append(p)
                num = num / p
                break
            if p > num:
                print 'No further prime factor found, factors so far: %s' % pf
                return None

factors = prime_factors(600851475143)
print factors

