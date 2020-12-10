import unittest
from bstInsertion import Bst
from traversals import in_order_traversal


class TestTree(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestTree, self).__init__()

    def test_tree_one(self):
        bst = Bst()
        bst.insert(5)
        bst.insert(2)
        bst.insert(8)
        bst.insert(1)
        bst.insert(3)
        print(in_order_traversal(bst.root))

    def test_tree_two(self):
        bst1 = Bst()
        bst1.insert(1)
        bst1.insert(2)
        bst1.insert(3)
        bst1.insert(4)
        bst1.insert(5)
        print(in_order_traversal(bst1.root))


def main():
    tt = TestTree()
    tt.test_tree_one()
    tt.test_tree_two()


if __name__ == "__main__":
    main()
