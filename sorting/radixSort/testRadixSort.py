import unittest
from radixSort import RadixSort


class TestRadixSort(unittest.TestCase):

    def testRadixSort(self):
        radix_sort = RadixSort()
        self.assertRaises(TypeError, radix_sort.radixSort, None)

        self.assertEqual(radix_sort.radixSort([]), [])

        data = [128, 256, 164, 8, 2, 148, 212, 242, 244]
        expected = [2, 8, 128, 148, 164, 212, 242, 244, 256]

        self.assertEqual(radix_sort.radixSort(data), expected)

        print('Success: test_radix_sort \n')


def main():
    test = TestRadixSort()
    # radix_sort = RadixSort()
    test.testRadixSort()


if __name__ == "__main__":
    main()
