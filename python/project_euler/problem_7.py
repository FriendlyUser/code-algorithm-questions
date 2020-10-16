# brute force find 10 001st prime number

import itertools
from math import sqrt

# Tests whether the given integer is a prime number.
def is_prime(x):
    if x <= 1:
        return False
    elif x <= 3:
        return True
    elif x % 2 == 0:
        return False
    else:
        for i in range(3, int(sqrt(x) + 1), 2):
            if x % i == 0:
                return False
        return True


# Computers are fast, so we can implement this solution by testing each number
# individually for primeness, instead of using the more efficient sieve of Eratosthenes.
#
# The algorithm starts with an infinite stream of incrementing integers starting at 2,
# filters them to keep only the prime numbers, drops the first 10000 items,
# and finally returns the first item thereafter.

ans = next(itertools.islice(filter(is_prime, itertools.count(2)), 10000, None))

print(str(ans))
