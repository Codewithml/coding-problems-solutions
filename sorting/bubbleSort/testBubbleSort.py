import unittest
from bubbleSort import BubbleSort


class TestBubbleSort(unittest.TestCase):

    def testBubbleSort(self, func):
        print('None output')
        self.assertRaises(TypeError, func, None)

        print('Empty input')
        self.assertEqual(func([]), [])

        print('One element')
        self.assertEqual(func([4]), [4])

        print('More than two elements')
        data = [19, 4, -1, -10, 21, 6, 2]
        self.assertEqual(func(data), sorted(data))

        print('Success: test_bubble_sort \n')


def main():
    test = TestBubbleSort()
    bubble_sort = BubbleSort()
    test.testBubbleSort(bubble_sort.bubbleSort)


if __name__ == "__main__":
    main()
