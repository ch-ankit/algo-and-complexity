import unittest

from sort import insertion_sort, merge
from sort import merge_sort

class SearchTestCase(unittest.TestCase):
    given_list_unsorted=[2,5,6,9,8,0]
    given_list_sorted=[0,2,5,6,8,9]
    given_list_reverse_sorted=[9,8,7,6,5,4,3,2,1]

    def test_insertion_sort(self):
        self.assertListEqual(insertion_sort(self.given_list_unsorted[:]),[0,2,5,6,8,9])
        self.assertListEqual(insertion_sort(self.given_list_sorted[:]),[0,2,5,6,8,9])
        self.assertListEqual(insertion_sort(self.given_list_reverse_sorted[:]),[1,2,3,4,5,6,7,8,9])

    def test_merge(self):
        self.assertListEqual(merge(self.given_list_unsorted[:],0,1,1),[2,5,6,9,8,0])
        self.assertListEqual(merge(self.given_list_unsorted[:],1,2,2),[2,5,6,9,8,0])
        self.assertListEqual(merge(self.given_list_sorted[:],0,2,5),[0,2,5,6,8,9])
        
    def test_merge_sort(self):
        self.assertListEqual(merge_sort(self.given_list_unsorted[:],0,5),[0,2,5,6,8,9])
        self.assertListEqual(merge_sort(self.given_list_sorted[:],0,5),[0,2,5,6,8,9])
        self.assertListEqual(merge_sort(self.given_list_reverse_sorted[:],0,8),[1,2,3,4,5,6,7,8,9])

if __name__ == '__main__':
    unittest.main()