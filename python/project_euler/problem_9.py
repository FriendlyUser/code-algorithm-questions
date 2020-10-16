"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

See https://projecteuler.net/problem=9
"""
import math

# since the triplet is a + b + c = 1000
# only go to 500
# brute force
abc = 0
PERIMETER = 1000
for a in range(1, PERIMETER + 1):
    for b in range(a + 1, PERIMETER + 1):
        c = PERIMETER - a - b
        if a * a + b * b == c * c:
            # It is now implied that b < c, because we have a > 0
            abc = a * b * c

print(str(abc))