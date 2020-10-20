# Binary search python
def find_low_index(arr, key):
    # TODO: Write - Your - Code
    low = 0
    high = len(arr) - 1
    mid = int(high / 2)

    while low <= high:
        mid_elem = arr[mid]

        if mid_elem < key:
            low = mid + 1
        else:
            high = mid - 1

        mid = low + int((high - low) / 2)

    if low < len(arr) and arr[low] == key:
        return low
    return -1


def find_high_index(arr, key):
    # TODO: Write - Your - Code
    low = 0
    high = len(arr) - 1
    mid = int(high / 2)
    while low <= high:
        mid_elem = arr[mid]
        if mid_elem <= key:
            low = mid + 1
        else:
            high = mid - 1

        mid = low + int((high - low) / 2)

    if high == -1:
        return -1

    if high < len(arr) and arr[high] == key:
        return high
    return -1


# def find_low_index(arr, key):
#     # TODO: Write - Your - Code
#     low = 0
#     high = len(arr) - 1
#     mid = int(high / 2)

#     # binary search on the array
#     while low < high:
#         mid_elem = arr[mid]

#         if mid_elem < key:
#             low = mid + 1
#         else:
#             high = mid - 1

#         mid = low + int((high - low) / 2)

#     if low < len(arr) and arr[low] == key:
#         return low
#     return -1


# def find_high_index(arr, key):
#     # TODO: Write - Your - Code
#     low = 0
#     high = len(arr) - 1
#     mid = int(high / 2)

#     while low < high:
#         mid_elem = arr[mid]

#         if mid_elem < key
#           low  = mid + 1
#         else:
#           high = mid - 1

#         mid = int((high - low) / 2)

#     if high == -1:
#       return high

#     if high < len(arr) and arr[high] == key:
#       return high
#     return -1
