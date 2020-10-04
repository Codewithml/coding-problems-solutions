import unittest
from stack import Stack, Node


class TestStack(unittest.TestCase):
    def test_end_to_end(self):
        print('Test: Empty stack')
        stack = Stack()
        self.assertAlmostEqual(len(stack), 0)
        # self.assertEqual(stack.getData(), )
        self.assertEqual(stack.peek(), None)
        self.assertEqual(stack.pop(), None)

        print('Test: One element')
        top = Node(5)
        stack = Stack(top)
        self.assertEqual(len(stack), 1)
        self.assertEqual(stack.getData(), None)
        self.assertEqual(stack.pop(), 5)
        self.assertEqual(stack.peek(), None)

        print('Test: More than one element')
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(len(stack), 3)
        self.assertEqual(stack.getData(), None)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(len(stack), 2)
        self.assertEqual(stack.peek(), 2)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(len(stack), 1)
        self.assertEqual(stack.peek(), 1)
        self.assertEqual(stack.isEmpty(), False)
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(len(stack), 0)
        self.assertEqual(stack.peek(), None)
        self.assertEqual(stack.isEmpty(), True)
        print('Success: test_end_to_end')


def main():
    test = TestStack()
    test.test_end_to_end()


if __name__ == '__main__':
    main()
