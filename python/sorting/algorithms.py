def bubble_sort(list):
    # Exchange the elements to arrage in order
    lastElementIndex = len(list)-1
    for passNo in range(lastElementIndex, 0, -1):
      for idx in range(passNo):
        if list[idx] > list[idx+1]:
          # Swap elements
          list[idx], list[idx+1]=list[idx+1], list[idx]
    return list

def insertion_sort(list):
  for i in range(1, len(list)):
    j = i-1
    element_next = list[i]
    while (list[j] > element_next) and (j >= 0):
      list[j+1] = list[j]
      j=j-1
    list[j+1] = element_next
  return list