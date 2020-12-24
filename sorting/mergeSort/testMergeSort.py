import unittest
from mergeSort import MergeSort


class TestMergeSort(unittest.TestCase):

    def testMergeSort(self, func):
        print('None output')
        self.assertRaises(TypeError, func, None)

        print('Empty input')
        self.assertEqual(func([]), [])

        print('One element')
        self.assertEqual(func([4]), [4])

        print('More than two elements')
        data = [5, 1, 7, 2, 6, -3, 5, 7, -1]
        self.assertEqual(func(data), sorted(data))

        print('Success: test_merge_sort \n')


def main():
    test = TestMergeSort()
    merge_sort = MergeSort()
    test.testMergeSort(merge_sort.mergeSort)


if __name__ == "__main__":
    main()
