"""

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

See https://projecteuler.net/problem=2
"""


def fib(n):
    if n == 0:
        return 1
    if n == 1:
        return 1

    return fib(n - 1) + fib(n - 2)


total_sum = 0
curr_value = 0
counter = 1
while curr_value < 4 * 1000000:
    curr_value = fib(counter)
    if curr_value % 2 == 0:
        total_sum = total_sum + curr_value
    counter = counter + 1

print(total_sum)
