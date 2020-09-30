import unittest
from compressString import CompressString


class TestCompress(unittest.TestCase):

    def testCompress(self, func):
        self.assertEqual(func(None), None)
        self.assertEqual(func(''), '')
        self.assertEqual(func('AABBCC'), 'AABBCC')
        self.assertEqual(func('AAABCCDDDDEE'), 'A3BC2D4EE')
        self.assertEqual(func('BAAACCDDDD'), 'BA3C2D4')
        self.assertEqual(func('AAABAACCDDDD'), 'A3BA2C2D4')
        print('Success: testCompress')


def main():
    test = TestCompress()
    compress_string = CompressString()
    test.testCompress(compress_string.compress)


if __name__ == '__main__':
    main()
