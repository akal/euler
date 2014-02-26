from common.primes import primes_func

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

