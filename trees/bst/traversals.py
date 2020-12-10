def in_order_traversal(node):
    if node is not None:
        in_order_traversal(node.left)
        print(node.data)
        in_order_traversal(node.right)
