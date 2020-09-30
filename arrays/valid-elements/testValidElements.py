import unittest
from validElements import ValidElements


class TestValidElements(unittest.TestCase):
    def testValidElements(self, func):
        self.assertEqual(func([2, 2, 3, 3, 4, 5]), 4)
        self.assertEqual(func([1, 2, 3, 4, 4, 5, 5, 5]), 5)
        self.assertEqual(func([1, 1, 1, 2, 5, 5, 5]), 3)
        print("All test cases passed")


def main():
    test = TestValidElements()
    elements = ValidElements()
    test.testValidElements(elements.validElements)
    test.testValidElements(elements.validElements2)
    test.testValidElements(elements.validElements3)


if __name__ == "__main__":
    main()
