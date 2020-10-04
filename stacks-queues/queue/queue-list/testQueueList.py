import unittest
from queueList import Queue


class TestQueueList(unittest.TestCase):
    def testQueue(self):
        print('Test: Empty Queue')
        queue = Queue()
        self.assertEqual(queue.dequeue(), None)
        self.assertEqual(queue.size(), 0)
        self.assertEqual(queue.isEmpty(), True)

        print('Test: One element')
        queue = Queue()
        queue.enqueue(5)
        self.assertEqual(queue.size(), 1)
        self.assertEqual(queue.dequeue(), 5)
        self.assertEqual(queue.isEmpty(), True)

        print('Test: Multiple elements')
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual(queue.size(), 3)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.isEmpty(), False)
        self.assertEqual(queue.dequeue(), 3)
        self.assertEqual(queue.isEmpty(), True)
        print('Success: testQueue')


def main():
    test = TestQueueList()
    test.testQueue()


if __name__ == '__main__':
    main()
