from itertools import groupby


def prime_factor(n):
    factors = []
    d = 2
    while n > 1:
        if n % d == 0:
            factors.append(d)
            n = n / d
        else:
            d += 1
    return factors

max_factors = {}
for n_factors in map(prime_factor, range(2, 21)):
    for p, grp in groupby(n_factors):
        cnt = len(list(grp))
        if max_factors.get(p, 0) < cnt:
            max_factors[p] = cnt

print reduce(lambda x, y: x * y, 
             [int(math.pow(a, n))
              for a, n in max_factors.items()])

