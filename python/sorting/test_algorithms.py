import unittest
from sorting.algorithms import bubble_sort, insertion_sort
class TestSorting(unittest.TestCase):
    def setUp(self):
        self.newList = [25, 21, 22, 24, 23, 27, 26]
        self.sortedList = [21, 22, 23, 24, 25, 26, 27]
    def test_bubble_sort(self):
        sortedList = bubble_sort(self.newList)
        self.assertEqual(sortedList, self.sortedList)

    def test_insertion_sort(self):
        sortedList = insertion_sort(self.newList)
        self.assertEqual(sortedList, self.sortedList)

if __name__ == '__main__':
    unittest.main()
  