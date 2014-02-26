import math

def is_palindrome(p):
    return str(p) == str(p)[::-1]

maxpal = 0
for a, b in [(n,m) 
             for n in range(999, 100, -1) 
             for m in range(999, n - 1, -1)]:
    if is_palindrome(a * b) and a * b > maxpal:
        maxpal = a * b
print maxpal

             

