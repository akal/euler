fib = [1, 2]
while True:
    next = fib[-1] + fib[-2]
    if next > 4000000:
        break
    fib.append(next)
print sum(filter(lambda x: x % 2 == 0, fib))
