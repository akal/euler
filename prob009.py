for a in range(3, 1001):
    for b in range(a, 1001):
        for c in range(b, 1001):
            if a + b + c > 1000:
                break
            if (a + b + c == 1000
                and a * a + b * b == c * c):
                print 'a:%d, b:%d, c:%d' % (a, b, c)
                print 'a * b * c: %d' % (a * b * c)
