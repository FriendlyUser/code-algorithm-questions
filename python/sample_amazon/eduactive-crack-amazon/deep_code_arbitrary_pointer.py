"""

LinkedListNode
"""

class LinkedListNode:
  def __init__(self, data)
    self.data = data
    self.arbitrary = None



def deep_copy_arbitrary_pointer(head):
  # Return in head is none
  if head == None:
    return head

  current=head
  new_head = None
  new_prev = None
  ht = dict()
  # iterate through the linked list
  while current != None:
    # create a copy node
    new_node = LinkedListNode(current.data)
    new_node.arbitrary = current.arbitrary
    # case where not head node
    if new_prev != None:
      new_prev.next = new_node
    # head node
    else:
      new_head = new_node
    # Add node to list
    ht[current] = new_node
    new_prev = new_node
    # Iterate to next node
    current = current.next
  
  new_current = new_head

  # iterate across cloned linked list 
  # and update arbitrary references
  while new_current != None:
    if new_current.arbitrary != None:
      node = ht[new_current.arbitrary]

      new_current.arbitrary = node
    new_current = new_current.next

  return new_head