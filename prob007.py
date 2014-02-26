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

primes = primes_func()
print list(itertools.islice(primes, 10001))[-1]

