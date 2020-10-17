"""
1. Find the missing number in the array
You are given an array of positive numbers from 1 to n, such that all numbers from 1 to n are present except one number x. You have to find x. The input array is not sorted.

3 7 1 2 8 4 5
n = 8, missing number = 6
"""


def find_missing(input):
    n = len(input) + 1
    n_sum = sum(input)
    expected_sum = n * (n + 1) / 2
    missing_int = expected_sum - n_sum
    return missing_int


input_list = [3, 7, 1, 2, 8, 4, 5]
find_missing(input_list)
