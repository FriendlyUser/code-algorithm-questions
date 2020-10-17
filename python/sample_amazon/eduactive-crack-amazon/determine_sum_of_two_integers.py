"""
2. Determine if the sum of two integers is equal to the given value
Given an array of integers and a value, determine if there are any two integers in the array whose sum is equal to the given value. Return true if the sum exists and return false if it does not. Consider this array and the target sums:
"""


def find_sum_in_two(A, val):
    found_values = set()
    for a in A:
        if val - a in found_values:
            return True
        found_values.add(a)
    return False


"""
Runtime Complexity: Linear, O(n)

Memory Complexity: Linear, O(n)

You can use the following algorithm to find a pair that add up to the target (say val).

Scan the whole array once and store visited elements in a hash set.
   scan, for every element e in the array, we check if val - e is present in the hash set i.e. val - e is already visited.
  If val - e is found in the hash set, it means there is a pair (e, val - e) in array whose sum is equal to the given val.
  If we have exhausted all elements in the array and didn’t find any such pair, the function will return false

"""


def merged_sorted(head1, head2):
    if head1 == None:
        return head2
    elif head2 == None:
        return head1

    mergedHead = None
    if head1.data <= head2.data:
        mergedHead = head1
    else:
        mergedHead = head2
        head2 = head2.next

    mergedTail = mergedHead

    while head1 != None and head2 != None:
        temp = None
        if head1.data <= head2.data:
            temp = head1
            head1 = head1.next
        else:
            temp = head2
            head2 = head2.next

        mergedTail.next = temp
        mergedTail = temp

    if head1 != None:
        mergedTail.next = head1
    elif head2 != None:
        mergedTail.next = head2

    return mergedHead


"""
Runtime Complexity: Linear, O(m + n)O(m+n) where m and n are lengths of both linked lists

Memory Complexity: Constant, O(1)O(1)

Maintain a head and a tail pointer on the merged linked list. Then choose the head of the merged linked list by comparing the first node of both linked lists. For all subsequent nodes in both lists, you choose the smaller current node and link it to the tail of the merged list, and moving the current pointer of that list one step forward.

Continue this while there are some remaining elements in both the lists. If there are still some elements in only one of the lists, you link this remaining list to the tail of the merged list. Initially, the merged linked list is NULL.

Compare the value of the first two nodes and make the node with the smaller value the head node of the merged linked list. In this example, it is 4 from head1. Since it’s the first and only node in the merged list, it will also be the tail. Then move head1 one step forward.
"""