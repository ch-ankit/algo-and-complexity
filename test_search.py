import unittest
from search import linenar_search
from search import binary_search


class SearchTestCase(unittest.TestCase):
    def test_linear_search(self):
        values = [2, 5, 20, 90, 99, 100]
        self.assertEqual(binary_search(values, 2), 0)
        self.assertEqual(binary_search(values, 5), 1)
        self.assertEqual(binary_search(values, 20), 2)
        self.assertEqual(binary_search(values, 100), 5)
        self.assertEqual(binary_search(values, 99), 4)
        self.assertEqual(binary_search(values, 90), 3)

    def test_binary_search(self):
        values = [2, 5, 20, 90, 99, 100]
        self.assertEqual(binary_search(values, 2), 0)
        self.assertEqual(binary_search(values, 5), 1)
        self.assertEqual(binary_search(values, 20), 2)
        self.assertEqual(binary_search(values, 100), 5)
        self.assertEqual(binary_search(values, 99), 4)
        self.assertEqual(binary_search(values, 90), 3)


if __name__ == '__main__':
    unittest.main()
