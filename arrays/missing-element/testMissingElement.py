import unittest
from missingElement import MissingElement


class TestMisssingElement(unittest.TestCase):
    def test_ele(self, sol):
        self.assertEqual(sol([5, 5, 7, 7], [5, 7, 7]), 5)
        self.assertEqual(sol([1, 2, 3, 4, 5, 6, 7],
                             [3, 7, 2, 1, 4, 6]), 5)
        self.assertEqual(sol([9, 8, 7, 6, 5, 4, 3, 2, 1],
                             [9, 8, 7, 5, 4, 3, 2, 1]), 6)
        print("All test cases passed")


def main():
    test = TestMisssingElement()
    element = MissingElement()
    test.test_ele(element.missingElement)
    test.test_ele(element.missingElement2)
    test.test_ele(element.missingElement3)
    test.test_ele(element.missingElement4)


if __name__ == "__main__":
    main()
