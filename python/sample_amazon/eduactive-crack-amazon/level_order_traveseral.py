"""
Runtime Complexity: Linear, O(n)O(n)

Memory Complexity: Linear, O(n)O(n)

Here, you are using two queues: current_queue and next_queue. You push the nodes in both queues alternately based on the current level number.

You’ll dequeue nodes from the current_queue, print the node’s data, and enqueue the node’s children to the next_queue. Once the current_queue becomes empty, you have processed all nodes for the current level_number. To indicate the new level, print a line break (\n), swap the two queues, and continue with the above-mentioned logic.

After printing the leaf nodes from the current_queue, swap current_queue and next_queue. Since the current_queue would be empty, you can terminate the loop.
"""

import threading, queue
import collections.deque


def level_order_traversal(root):
    if root == None:
        return
    result = ""
    queues = [deque(), deque()]

    current_queue = queues[0]
    next_queue = queues[1]

    current_queue.append(root)
    level_number = 0

    while current_queue:
        temp = current_queue.popleft()
        result += str(temp.data) + " "

        if temp.left != None:
            next_queue.append(temp.left)

        if temp.right != None:
            next_queue.append(temp.right)

        if not current_queue:
            level_number += 1
            current_queue = queues[level_number % 2]
            next_queue = queues[(level_number + 1) % 2]

    # TODO: Write - Your - Code
    return result
