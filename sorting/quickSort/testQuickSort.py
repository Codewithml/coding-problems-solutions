import unittest
from quickSort import QuickSort


class TestQuickSort(unittest.TestCase):

    def testQuickSort(self, func):
        print('None output')
        self.assertRaises(TypeError, func, None)

        print('Empty input')
        self.assertEqual(func([]), [])

        print('One element')
        self.assertEqual(func([4]), [4])

        print('More than two elements')
        data = [5, 1, 7, 2, 6, -3, 5, 7, -1]
        self.assertEqual(func(data), sorted(data))

        print('Success: test_quick_sort \n')


def main():
    test = TestQuickSort()
    quick_sort = QuickSort()
    test.testQuickSort(quick_sort.quickSort)


if __name__ == "__main__":
    main()
