import unittest
from insertionSort import InsertionSort


class TestInsertionSort(unittest.TestCase):

    def testInsertionSort(self, func):
        print('None output')
        self.assertRaises(TypeError, func, None)

        print('Empty input')
        self.assertEqual(func([]), [])

        print('One element')
        self.assertEqual(func([4]), [4])

        print('More than two elements')
        data = [5, 4, 3, 2, 1]
        self.assertEqual(func(data), sorted(data))

        print('Success: test_insertion_sort \n')


def main():
    test = TestInsertionSort()
    insertion_sort = InsertionSort()
    test.testInsertionSort(insertion_sort.insertionSort)


if __name__ == "__main__":
    main()
