"""
 Find all subsets of a given set of integers
We are given a set of integers and we have to find all the possible subsets of this set of integers. The following example elaborates on this further
"""


def get_bit(num, bit):
    temp = 1 << bit
    temp = temp & num
    if temp == 0:
        return 0
    return 1


def get_all_subsets(v, sets):
    subset_counts = 2 ** len(v)
    for i in range(0, subset_counts):
        st = set([])
        for j in range(i, len(v)):
            if get_bit(i, j):
                st.append(v[j])
        sets.append(st)
    return sets


# def get_bit(num, bit):
#     temp = 1 << bit
#     bit_value = temp & num
#     if bit_value == 0:
#         return 0
#     return 1


# def get_all_subsets(v, sets):
#     # TODO: Write - Your - Code
#     num_subsets = 2 ** len(v)
#     for i in range(0, num_subsets):
#         st = set([])
#         for j in range(i, len(v)):
#             if get_bit(i, j) == 1:
#                 st.append(v[i])
#         sets.append(st)
#     return sets
