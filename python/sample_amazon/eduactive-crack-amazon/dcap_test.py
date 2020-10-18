class LinkedListNode:
  def __init__(self, data)
    self.data = data
    self.arbitrary = None

def deep_copy_arbitrary_pointer(head):
    # TODO: Write - Your - Code
    if head == None:
      return head

    current = head 
    new_head = None
    new_prev = None
    ht = dict()
    # iterate across old linked list
    if current != None:
      new_node = LinkedListNode(current.data)
      new_node.arbitrary = current.arbitrary
      if new_prev != None:
        new_prev.next = new_node
      else:
        new_head = new_node
      
      ht[current] = new_node
      new_prev = new_node
      current = current.next

    new_current = new_head 

    # iterate across new linked list
    while new_current != None:
      if new_current.arbitrary != None:
        # update the arbitrary pointer
        new_current.arbitrary = ht[new_current.arbitrary]
      new_current = new_current.next
    return None
