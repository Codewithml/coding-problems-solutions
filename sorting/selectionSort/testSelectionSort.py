import unittest
from selectionSort import SelectionSort


class TestSelectionSort(unittest.TestCase):

    def testSelectionSort(self, func):
        print('None output')
        self.assertRaises(TypeError, func, None)

        print('Empty input')
        self.assertEqual(func([]), [])

        print('One element')
        self.assertEqual(func([4]), [4])

        print('More than two elements')
        data = [19, 4, -1, -10, 21, 6, 2]
        self.assertEqual(func(data), sorted(data))

        print('Success: test_selection_sort \n')


def main():
    test = TestSelectionSort()
    selection_sort = SelectionSort()
    test.testSelectionSort(selection_sort.selectionSort)


if __name__ == "__main__":
    main()
