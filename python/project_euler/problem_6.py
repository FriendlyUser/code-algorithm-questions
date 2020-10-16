"""
https://projecteuler.net/problem=6
"""

list_of_num = [x for x in range(1, 101)]
list_of_squares = [x ** 2 for x in list_of_num]

square_of_sum = sum(list_of_num) ** 2

sum_of_squares = sum(list_of_squares)

diff = square_of_sum - sum_of_squares

print(str(diff))