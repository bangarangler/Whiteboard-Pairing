def recursive_depth_first_for_each(node, cb):
    cb(node.value)

    if node.left:
        recursive_depth_first_for_each(node.left, cb)

    if node.right:
        iterative_depth_first_for_each(node.right, cb)

def iterative_depth_first_for_each(node, cb):
    stack = []
    stack.append(node)

    while len(stack) > 0:
        current = stack.pop()

        if current.right:
            stack.append(current.right)

        if current.left:
            stack.append(current.left)

        cb(current.value)

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

root = BinaryTreeNode(6)
root.insert_left(10)
root.insert_right(18)
root.left.insert_left(9)
root.right.insert_right(89)

cb = lambda x: print(x)

recursive_depth_first_for_each(root, cb)  # should print 6 10 9 18 89
print()
iterative_depth_first_for_each(root, cb)  # should print 6 10 9 18 89
print()

root.left.insert_right(15)
root.right.insert_left(0)

recursive_depth_first_for_each(root, cb)  # should print 6 10 9 15 18 0 89
print()
iterative_depth_first_for_each(root, cb)  # should print 6 10 9 15 18 0 89
print()
