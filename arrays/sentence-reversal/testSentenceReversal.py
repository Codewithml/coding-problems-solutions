import unittest
from sentenceReversal import SentenceReversal


class TestSentenceReversal(unittest.TestCase):
    def testSentenceReversal(self, func):
        self.assertEqual(func(None), None)
        self.assertEqual(func('   space before plague'), 'plague before space')
        self.assertEqual(func('space after    '), 'after space')
        self.assertEqual(func(' Hello John  how are you   ?'),
                         '? you are how John Hello')
        self.assertEqual(func('1'), '1')
        print("ALL TEST CASES PASSED")


def main():
    test = TestSentenceReversal()
    sent = SentenceReversal()
    test.testSentenceReversal(sent.sentenceReversal)
    test.testSentenceReversal(sent.sentenceReversal2)
    test.testSentenceReversal(sent.sentenceReversal3)


if __name__ == "__main__":
    main()
