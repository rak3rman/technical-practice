import unittest
from array import Array


class TestArray(unittest.TestCase):

    def test_len(self):
        arr1 = Array()
        self.assertEqual(len(arr1), 0)

    def test_append(self):
        arr1 = Array()
        arr1.append(1)
        self.assertEqual(len(arr1), 1)
        self.assertEqual(arr1[0], 1)


if __name__ == '__main__':
    unittest.main()
